from flask import Blueprint, request, jsonify
from ...application.services.category_service import CategoryService
from ...domain.schemas.category_schema import category_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.http.swagger.category_swagger import create_category_swagger

category_urls = Blueprint('category_blueprint', __name__)


@category_urls.route('/create', methods=['POST'])
@swag_from(create_category_swagger)
def create_category():
    try:
        data = request.get_json()
        name = data.get('name')

        # Create Category
        new_category = CategoryService.create_category(name)

        # Serialize schema
        result = category_schema.dump(new_category)

        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
