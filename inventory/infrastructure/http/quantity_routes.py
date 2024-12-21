from flask import Blueprint, request, jsonify
from ...application.services.quantity_service import QuantityService
from ...domain.schemas.quantity_schema import quantity_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.http.swagger.quantity_swagger import create_quantity_swagger

quantity_urls = Blueprint('quantity_blueprint', __name__)


@quantity_urls.route('/create', methods=['POST'])
@swag_from(create_quantity_swagger)
def create_quantity():
    try:
        data = request.get_json()
        initial_quantity = data.get('initial_quantity')
        progress_quantity = data.get('progress_quantity')

        # Validate initial_quantity
        if initial_quantity < 0:
            return jsonify(
                {
                    "error": "Initial quantity can't be negative."
                }
            ), 400

        # Validate progress_quantity
        if progress_quantity < 0:
            return jsonify(
                {
                    "error": "Progress quantity can't be negative."
                }
            ), 400

        if initial_quantity < progress_quantity:
            return jsonify(
                {
                    "error": "Initial quantity can't be less than progress quantity."
                }
            ), 400

        # Create Quantity
        new_quantity = QuantityService.create_quantity(
            initial_quantity, progress_quantity)

        # Serialize schema
        result = quantity_schema.dump(new_quantity)

        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
