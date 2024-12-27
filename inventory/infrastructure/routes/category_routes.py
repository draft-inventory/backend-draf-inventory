import re

from flask import Blueprint, request, jsonify
from ...application.services.category_service import CategoryService
from ...domain.schemas.category_schema import category_schema, category_list_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.routes.swagger.category_swagger import *

category_urls = Blueprint('category_blueprint', __name__)


# Regex para nombres válidos
VALID_NAME_REGEX = r"^[A-Za-zÁÉÍÓÚÑáéíóúñ ]{2,15}$"

@category_urls.route('/create', methods=['POST'])
@swag_from(create_category_swagger)
def create_category():
    try:
        data = request.get_json()
        name = data.get('name')

        # Validate name
        if not name or not re.match(VALID_NAME_REGEX, name):
            return jsonify(
                {
                    "error": "Invalid name. Name must be 2-15 characters, no numbers, and only valid Latin characters."
                }
            ), 400

        # Create Category
        new_category = CategoryService.create_category(name)

        # Serialize schema
        result = category_schema.dump(new_category)

        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500

@category_urls.route('/<int:category_id>', methods=['GET'])
@swag_from(get_category_by_id_swagger)
def get_category_by_id(category_id):
    try:
        # Retrieve category
        category = CategoryService.get_category_by_id(category_id)
        if not category:
            return jsonify({"error": "Category not found"}), 404

        # Serialize schema
        result = category_schema.dump(category)
        return jsonify(result), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


@category_urls.route('/all', methods=['GET'])
@swag_from(get_all_categories_swagger)
def get_all_categories():
    try:
        # Retrieve all categories
        categories = CategoryService.get_all_categorys()

        # Serialize schema
        result = category_list_schema.dump(categories)
        return jsonify(result), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


@category_urls.route('/<int:category_id>', methods=['PUT'])
@swag_from(update_category_swagger)
def update_category(category_id):
    try:
        data = request.get_json()
        name = data.get('name')

        # Validate name
        if not name or not re.match(VALID_NAME_REGEX, name):
            return jsonify(
                {
                    "error": "Invalid name. Name must be 2-15 characters, no numbers, and only valid Latin characters."
                }
            ), 400

        # Update Category
        updated_category = CategoryService.update_category(category_id, name)
        if not updated_category:
            return jsonify({"error": "Category not found"}), 404

        # Serialize schema
        result = category_schema.dump(updated_category)
        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


@category_urls.route('/<int:category_id>', methods=['DELETE'])
@swag_from(delete_category_swagger)
def delete_category(category_id):
    try:
        # Delete category
        deleted_category = CategoryService.delete_category(category_id)
        if not deleted_category:
            return jsonify({"error": "Category not found"}), 404

        return jsonify({"message": "Category deleted successfully"}), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500