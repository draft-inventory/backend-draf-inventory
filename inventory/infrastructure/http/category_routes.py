from flask import Blueprint, request, jsonify
from application.services.category_service import CategoryService
from domain.schemas.category_schema import category_schema

category_urls = Blueprint('category_blueprint', __name__)

@category_urls('/create', methods=['POST'])
def create_category():
    try:
        data = request.get_json()
        name = data.get('name')

        #Create Category
        new_category = CategoryService.create_category(name)

        #Serialyze schema
        result = category_schema.dump(new_category)
    
        return jsonify(result), 201
    
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
