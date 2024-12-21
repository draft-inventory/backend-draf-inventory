from flask import Blueprint, request, jsonify
from ...application.services.quantity_history_service import QuantityHistoryService
from ...application.services.quantity_service import QuantityService
from ...domain.schemas.quantity_history_schema import quantity_history_schema, quantity_history_list_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.http.swagger.quantity_history_swagger import *

quantity_history_urls = Blueprint('quantity_history_blueprint', __name__)


@quantity_history_urls.route('/create', methods=['POST'])
@swag_from(create_quantity_history_swagger)
def create_quantity_history():
    try:
        data = request.get_json()
        quantity_id = data.get('quantity_id')
        date = data.get('date')
        sold_quantity = data.get('sold_quantity')
        remaining_quantity = data.get('remaining_quantity')

        # Validar entradas
        if not quantity_id:
            return jsonify(
                {
                    "error": "Quantity ID can't be empty."
                }
            ), 400

        if not date:
            return jsonify(
                {
                    "error": "Date can't be empty."
                }
            ), 400

        if sold_quantity < 0:
            return jsonify(
                {
                    "error": "Sold quantity can't be negative."
                }
            ), 400

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


@quantity_history_urls.route('/all', methods=['GET'])
@swag_from(get_all_quantity_histories_swagger)
def get_all_quantity_histories():
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


@quantity_history_urls.route('/<int:quantity_history_id>', methods=['GET'])
@swag_from(get_quantity_history_by_id_swagger)
def get_quantity_history_by_id(quantity_history_id):
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


@quantity_history_urls.route('/quantity/<int:quantity_id>', methods=['GET'])
@swag_from(get_quantity_by_quiantity_id_swagger)
def get_quantity_by_quiantity_id(quantity_id):
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


@quantity_history_urls.route('/<int:quantity_history_id>', methods=['DELETE'])
@swag_from(delete_quantity_history_swagger)
def delete_quantity_history(quantity_history_id):
    try:
        quantity_history = QuantityHistoryService.delete_quantity_history(
            quantity_history_id)
        if not quantity_history:
            return jsonify({"error": "Quantity history not found."}), 404

        return jsonify({"message": "Quantity history deleted successfully"}), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500


@quantity_history_urls.route('/<int:quantity_history_id>', methods=['PUT'])
@swag_from(update_quantity_history_swagger)
def update_quantity_history(quantity_history_id):
    try:
        data = request.get_json()
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


@quantity_history_urls.route('/<int:quantity_history_id>', methods=['PATCH'])
@swag_from(patch_quantity_history_swagger)
def patch_quantity_history(quantity_history_id):
    try:
        data = request.get_json()
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
