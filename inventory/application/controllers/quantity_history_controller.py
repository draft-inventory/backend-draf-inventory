from flask import jsonify
from ...application.services.quantity_service import QuantityService
from ...application.services.quantity_history_service import QuantityHistoryService
from ...domain.schemas.quantity_history_schema import quantity_history_schema, quantity_history_list_schema

def create_quantity_history(data):
    """
    Lógica para crear un QuantityHistory.
    """
    try:
        quantity_id = data.get('quantity_id')
        date = data.get('date')
        sold_quantity = data.get('sold_quantity')
        remaining_quantity = data.get('remaining_quantity')

        # Validar entradas
        if not quantity_id:
            return jsonify({"error": "Quantity ID can't be empty."}), 400

        if not date:
            return jsonify({"error": "Date can't be empty."}), 400

        if sold_quantity < 0:
            return jsonify({"error": "Sold quantity can't be negative."}), 400

        # Recuperar el Quantity
        quantity = QuantityService.get_quantity_by_id(quantity_id)
        if not quantity:
            return jsonify({"error": "Quantity not found."}), 404

        # Validar que sold_quantity no sea mayor que progress_quantity
        if sold_quantity > quantity.progress_quantity:
            return jsonify(
                {
                    "error": "Sold quantity can't be greater than progress quantity."
                }
            ), 400

        # Calcular el nuevo remaining_quantity
        remaining_quantity = quantity.progress_quantity - sold_quantity

        # Actualizar progress_quantity con el nuevo remaining_quantity
        QuantityService.update_progress_quantity(
            quantity_id, remaining_quantity)

        # Crear el registro en QuantityHistory
        new_quantity_history = QuantityHistoryService.create_quantity_history(
            quantity_id, date, sold_quantity, remaining_quantity
        )

        # Serializar resultado
        result = quantity_history_schema.dump(new_quantity_history)

        return jsonify(result), 201
    except ValueError as ex:
        return jsonify(
            {
                "error": str(ex)
            }
        ), 400
    except Exception as ex:
        return jsonify(
            {
                "error": "Internal error", "exception": str(ex)
            }
        ), 500
    
def get_all_quantity_histories():
    """
    Lógica para listar todos los QuantityHistory.
    """
    try:
        quantity_histories = QuantityHistoryService.get_all_quantity_histories()
        result = quantity_history_list_schema.dump(quantity_histories)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify(
            {
                "error": "Internal error", "exception": str(ex)
            }
        ), 500

def get_quantity_history_by_id(quantity_history_id):
    """
    Lógica para obtener un QuantityHistory por su ID.
    """
    try:
        quantity_history = QuantityHistoryService.get_quantity_history_by_id(
            quantity_history_id)
        if not quantity_history:
            return jsonify(
                {
                    "error": "Quantity history not found."
                }
            ), 404

        result = quantity_history_schema.dump(quantity_history)

        return jsonify(result), 200

    except Exception as ex:
        return jsonify(
            {
                "error": "Internal error", "exception": str(ex)
            }
        ), 500

def get_quantity_by_quantity_id(quantity_id):
    """
    Lógica para obtener un QuantityHistory por su Quantity ID.
    """
    try:
        quantity_history = QuantityHistoryService.get_quantity_history_by_quantity_id(
            quantity_id)
        if not quantity_history:
            return jsonify(
                {
                    "error": "Quantity history not found."
                }
            ), 404

        result = quantity_history_list_schema.dump(quantity_history)

        return jsonify(result), 200

    except Exception as ex:
        return jsonify(
            {
                "error": "Internal error", "exception": str(ex)
            }
        ), 500
    
def update_quantity_history(quantity_history_id, data):
    """
    Lógica para actualizar un QuantityHistory.
    """
    try:
        quantity_id = data.get('quantity_id')
        date = data.get('date')
        sold_quantity = data.get('sold_quantity')
        remaining_quantity = data.get('remaining_quantity')

        # Validar que el registro exista
        quantity_history = QuantityHistoryService.get_quantity_history_by_id(
            quantity_history_id)
        if not quantity_history:
            return jsonify({"error": "Quantity history not found."}), 404

        # Validar entradas
        if not quantity_id:
            return jsonify({"error": "Quantity ID can't be empty."}), 400

        if not date:
            return jsonify({"error": "Date can't be empty."}), 400

        if sold_quantity is None or sold_quantity < 0:
            return jsonify({"error": "Sold quantity can't be negative."}), 400

        # Recuperar el Quantity relacionado
        quantity = QuantityService.get_quantity_by_id(quantity_id)
        if not quantity:
            return jsonify({"error": "Quantity not found."}), 404

        # Validar que sold_quantity no sea mayor que progress_quantity
        if sold_quantity > quantity.progress_quantity:
            return jsonify({"error": "Sold quantity can't be greater than progress quantity."}), 400

        # Calcular el nuevo remaining_quantity
        remaining_quantity = quantity.progress_quantity - sold_quantity

        # Actualizar progress_quantity con el nuevo remaining_quantity
        QuantityService.update_progress_quantity(
            quantity_id, remaining_quantity)

        # Actualizar el registro en QuantityHistory
        updated_quantity_history = QuantityHistoryService.update_quantity_history(
            quantity_history_id, quantity_id, date, sold_quantity, remaining_quantity
        )

        # Serializar resultado
        result = quantity_history_schema.dump(updated_quantity_history)

        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500
    
def delete_quantity_history(quantity_history_id):
    """
    Lógica para eliminar un QuantityHistory.
    """
    try:
        quantity_history = QuantityHistoryService.delete_quantity_history(
            quantity_history_id)
        if not quantity_history:
            return jsonify({"error": "Quantity history not found."}), 404

        return jsonify({"message": "Quantity history deleted successfully"}), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500
    
def patch_quantity_history(quantity_history_id, data):
    try:
        quantity_id = data.get('quantity_id')
        date = data.get('date')
        sold_quantity = data.get('sold_quantity')

        # Validar que el registro exista
        quantity_history = QuantityHistoryService.get_quantity_history_by_id(
            quantity_history_id)
        if not quantity_history:
            return jsonify({"error": "Quantity history not found."}), 404

        # Validar entradas
        if quantity_id is not None and not quantity_id:
            return jsonify({"error": "Quantity ID can't be empty."}), 400

        if date is not None and not date:
            return jsonify({"error": "Date can't be empty."}), 400

        if sold_quantity is not None and sold_quantity < 0:
            return jsonify({"error": "Sold quantity can't be negative."}), 400

        # Recuperar el Quantity relacionado si se modifica quantity_id o sold_quantity
        if quantity_id is not None or sold_quantity is not None:
            quantity = QuantityService.get_quantity_by_id(
                quantity_id or quantity_history.quantity_id)
            if not quantity:
                return jsonify({"error": "Quantity not found."}), 404

            # Validar que sold_quantity no sea mayor que progress_quantity
            if sold_quantity is not None and sold_quantity > quantity.progress_quantity:
                return jsonify({"error": "Sold quantity can't be greater than progress quantity."}), 400

            # Calcular el nuevo remaining_quantity si sold_quantity se modifica
            if sold_quantity is not None:
                remaining_quantity = quantity.progress_quantity - sold_quantity

                # Actualizar progress_quantity con el nuevo remaining_quantity
                QuantityService.update_progress_quantity(
                    quantity_id or quantity_history.quantity_id, remaining_quantity
                )

                # Añadir remaining_quantity al conjunto de campos a actualizar
                data['remaining_quantity'] = remaining_quantity

        # Actualizar el registro en QuantityHistory
        updated_quantity_history = QuantityHistoryService.patch_quantity_history(
            quantity_history_id, data
        )

        # Serializar resultado
        result = quantity_history_schema.dump(updated_quantity_history)

        return jsonify(result), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500