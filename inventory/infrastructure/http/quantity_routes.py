from flask import Blueprint, request, jsonify
from ...application.services.quantity_service import QuantityService
from ...domain.schemas.quantity_schema import quantity_schema, quantity_list_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.http.swagger.quantity_swagger import *

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


@quantity_urls.route('/all', methods=['GET'])
@swag_from(get_all_quantities_swagger)
def get_all_quantities():
    try:
        quantities = QuantityService.get_all_quantities()
        result = quantity_list_schema.dump(quantities)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


@quantity_urls.route('/<int:quantity_id>', methods=['GET'])
@swag_from(get_quantity_by_id_swagger)
def get_quantity_by_id(quantity_id):
    try:
        quantity = QuantityService.get_quantity_by_id(quantity_id)
        if not quantity:
            return jsonify(
                {
                    "error": "Quantity not found"
                }
            ), 404
        result = quantity_schema.dump(quantity)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify(
            {
                "error": "Internal error", "except": str(ex)
            }
        ), 500


@quantity_urls.route('/<int:quantity_id>', methods=['PUT'])
@swag_from(update_quantity_swagger)
def update_quantity(quantity_id):
    try:
        data = request.get_json()
        initial_quantity = data.get('initial_quantity')
        progress_quantity = data.get('progress_quantity')
        updated_quantity = QuantityService.update_quantity(
            quantity_id, initial_quantity, progress_quantity)

        if not updated_quantity:
            return jsonify({"error": "Quantity not found"}), 404

        result = quantity_schema.dump(updated_quantity)

        return jsonify(result), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


@quantity_urls.route('/<int:quantity_id>', methods=['DELETE'])
@swag_from(delete_quantity_swagger)
def delete_quantity(quantity_id):
    try:
        deleted_quantity = QuantityService.delete_quantity(quantity_id)
        if not deleted_quantity:
            return jsonify(
                {
                    "error": "Quantity not found"
                }
            ), 404
        return jsonify(
            {
                "message": "Quantity deleted successfully"
            }
        ), 200
    except Exception as ex:
        return jsonify(
            {
                "error": "Internal error", "except": str(ex)
            }
        ), 500

@quantity_urls.route('/<int:quantity_id>', methods=['PATCH'])
@swag_from(patch_quantity_swagger)
def patch_quantity(quantity_id):
    try:
        fields_to_update = request.get_json()
        updated_quantity = QuantityService.patch_quantity(quantity_id, fields_to_update)
        if not updated_quantity:
            return jsonify({"error": "Quantity not found"}), 404
        result = quantity_schema.dump(updated_quantity)
        return jsonify(result), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
