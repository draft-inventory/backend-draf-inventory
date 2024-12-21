from flask import Blueprint, request, jsonify
from ...application.services.quantity_history_service import QuantityHistoryService
from ...application.services.quantity_service import QuantityService
from ...domain.schemas.quantity_history_schema import quantity_history_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.http.swagger.quantity_history_swagger import create_quantity_history_swagger

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

        if remaining_quantity < 0:
            return jsonify(
                {
                    "error": "Remaining quantity can't be negative."
                }
            ), 400

        # Recuperar el Quantity
        quantity = QuantityService.get_quantity_by_id(quantity_id)
        if not quantity:
            return jsonify(
                {
                    "error": "Quantity not found."
                }
            ), 404

        # Validar relación entre remaining_quantity y initial_quantity
        if remaining_quantity > quantity.initial_quantity:
            return jsonify(
                {
                    "error": "Remaining quantity can't be greater than initial quantity."
                }
            ), 400


        # Actualizar progress_quantity
        new_progress_quantity = quantity.progress_quantity - sold_quantity
        QuantityService.update_progress_quantity(
            quantity_id, new_progress_quantity)

        # Crear el registro en QuantityHistory
        new_quantity_history = QuantityHistoryService.create_quantity_history(
            quantity_id, date, sold_quantity, remaining_quantity)

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
