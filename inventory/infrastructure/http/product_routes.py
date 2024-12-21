import re
from ...application.services.quantity_service import QuantityService
from ...application.services.category_service import CategoryService
from flask import Blueprint, request, jsonify
from ...application.services.product_service import ProductService
from ...domain.schemas.product_schema import product_schema, product_list_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.http.swagger.product_swagger import *

product_urls = Blueprint('product_blueprint', __name__)


# Swagger

product_urls = Blueprint('product_blueprint', __name__)


@product_urls.route('/create', methods=['POST'])
@swag_from(create_product_swagger)
def create_product():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        category_id = data.get('category_id')
        quantity_id = data.get('quantity_id')

        # Validar campo name (sin caracteres especiales ni números)
        if not re.match("^[A-Za-z\s]+$", name):
            return jsonify({"error": "Name must only contain alphabetic characters and spaces."}), 400

        # Validar campo description (sin caracteres especiales, pero permite números)
        if not re.match("^[A-Za-z0-9\s]+$", description):
            return jsonify({"error": "Description must only contain alphanumeric characters and spaces."}), 400

        # Validar existencia de category_id
        if not CategoryService.get_category_by_id(category_id):
            return jsonify({"error": f"Category with ID {category_id} does not exist."}), 400

        # Validar existencia de quantity_id
        if not QuantityService.get_quantity_by_id(quantity_id):
            return jsonify({"error": f"Quantity with ID {quantity_id} does not exist."}), 400

        # Generar product_code automáticamente (primer y último carácter del nombre en mayúsculas)
        product_code_base = f"{name[0].upper()}{name[-1].upper()}"
        product_code = product_code_base
        counter = 1

        # Verificar duplicados en product_code
        while ProductService.check_product_code_exists(product_code):
            product_code = f"{product_code_base}_{counter}"
            counter += 1

        expiration_date = data.get('expiration_date')
        location_id = data.get('location_id')

        # Crear Producto
        new_product = ProductService.create_product(
            name, description, product_code, expiration_date, location_id, category_id, quantity_id
        )

        # Serializar esquema
        result = product_schema.dump(new_product)
        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
