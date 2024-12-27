# quantity_controller.py
from flask import jsonify
from ...application.services.quantity_service import QuantityService
from ...domain.schemas.quantity_schema import quantity_schema, quantity_list_schema

def create_quantity(data):
    """
    Lógica para crear un Quantity.
    """
    try:
        initial_quantity = data.get('initial_quantity')

        # Validar initial_quantity
        if initial_quantity is None or initial_quantity < 0:
            return jsonify({"error": "Initial quantity can't be negative or empty."}), 400

        # Set progress_quantity = initial_quantity
        progress_quantity = initial_quantity

        # Crear Quantity en la base de datos
        new_quantity = QuantityService.create_quantity(initial_quantity, progress_quantity)

        # Serializar resultado
        result = quantity_schema.dump(new_quantity)
        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def get_all_quantities():
    """
    Lógica para listar todos los Quantity.
    """
    try:
        quantities = QuantityService.get_all_quantities()
        result = quantity_list_schema.dump(quantities)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def get_quantity_by_id(quantity_id):
    """
    Lógica para obtener un Quantity por su ID.
    """
    try:
        quantity = QuantityService.get_quantity_by_id(quantity_id)
        if not quantity:
            return jsonify({"error": "Quantity not found"}), 404
        result = quantity_schema.dump(quantity)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def update_quantity(quantity_id, data):
    """
    Lógica para actualizar un Quantity.
    """
    try:
        initial_quantity = data.get('initial_quantity')
        progress_quantity = data.get('progress_quantity')

        updated_quantity = QuantityService.update_quantity(
            quantity_id, initial_quantity, progress_quantity
        )
        if not updated_quantity:
            return jsonify({"error": "Quantity not found"}), 404

        result = quantity_schema.dump(updated_quantity)
        return jsonify(result), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def delete_quantity(quantity_id):
    """
    Lógica para eliminar un Quantity.
    """
    try:
        deleted_quantity = QuantityService.delete_quantity(quantity_id)
        if not deleted_quantity:
            return jsonify({"error": "Quantity not found"}), 404
        return jsonify({"message": "Quantity deleted successfully"}), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def patch_quantity(quantity_id, fields_to_update):
    """
    Lógica para hacer un PATCH a un Quantity.
    """
    try:
        updated_quantity = QuantityService.patch_quantity(quantity_id, fields_to_update)
        if not updated_quantity:
            return jsonify({"error": "Quantity not found"}), 404
        result = quantity_schema.dump(updated_quantity)
        return jsonify(result), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
