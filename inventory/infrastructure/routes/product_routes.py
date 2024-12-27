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


@product_urls.route('/all', methods=['GET'])
@swag_from(get_all_products_swagger)
def get_all_products():
    try:
        products = ProductService.get_all_products()
        result = product_list_schema.dump(products)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify(
            {
                "error": "Internal error", "exception": str(ex)
            }
        ), 500


@product_urls.route('/<int:product_id>', methods=['GET'])
@swag_from(get_product_by_id_swagger)
def get_product_by_id(product_id):
    try:
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return jsonify(
                {
                    "error": "Product not found"
                }
            ), 404

        result = product_schema.dump(product)

        return jsonify(result), 200
    except Exception as ex:
        return jsonify(
            {
                "error": "Internal error", "exception": str(ex)
            }
        ), 500


@product_urls.route('/<int:product_id>', methods=['PUT'])
@swag_from(update_product_swagger)
def update_product(product_id):
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        category_id = data.get('category_id')
        quantity_id = data.get('quantity_id')

        # Validar campo name (sin caracteres especiales ni números)
        if not re.match("^[A-Za-z\s]+$", name):
            return jsonify(
                {
                    "error": "Name must only contain alphabetic characters and spaces."
                }
            ), 400

        # Validar campo description (sin caracteres especiales, pero permite números)
        if not re.match("^[A-Za-z0-9\s]+$", description):
            return jsonify(
                {
                    "error": "Description must only contain alphanumeric characters and spaces."
                }
            ), 400

        # Validar existencia de category_id
        if not CategoryService.get_category_by_id(category_id):
            return jsonify(
                {
                    "error": f"Category with ID {category_id} does not exist."
                }
            ), 400

        # Validar existencia de quantity_id
        if not QuantityService.get_quantity_by_id(quantity_id):
            return jsonify(
                {
                    "error": f"Quantity with ID {quantity_id} does not exist."
                }
            ), 400

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

        # Actualizar Producto
        updated_product = ProductService.update_product(
            product_id, name, description, product_code, expiration_date, location_id, category_id, quantity_id
        )

        if not updated_product:
            return jsonify({"error": "Product not found"}), 404

        # Serializar esquema
        result = product_schema.dump(updated_product)
        return jsonify(result), 200

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


@product_urls.route('/<int:product_id>', methods=['PATCH'])
@swag_from(patch_product_swagger)
def patch_product(product_id):
    try:
        data = request.get_json()
        product = ProductService.get_product_by_id(product_id)

        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Actualizar los campos enviados en la solicitud
        if 'name' in data:
            name = data.get('name')
            if not re.match("^[A-Za-z\s]+$", name):
                return jsonify(
                    {
                        "error": "Name must only contain alphabetic characters and spaces."
                    }
                ), 400
            product.name = name

            # Actualizar automáticamente el product_code si cambia el name
            product_code_base = f"{name[0].upper()}{name[-1].upper()}"
            product_code = product_code_base
            counter = 1
            while ProductService.check_product_code_exists(product_code):
                product_code = f"{product_code_base}_{counter}"
                counter += 1
            product.product_code = product_code

        if 'description' in data:
            description = data.get('description')
            if not re.match("^[A-Za-z0-9\s]+$", description):
                return jsonify(
                    {
                        "error": "Description must only contain alphanumeric characters and spaces."
                    }
                ), 400
            product.description = description

        if 'category_id' in data:
            category_id = data.get('category_id')
            if not CategoryService.get_category_by_id(category_id):
                return jsonify(
                    {
                        "error": f"Category with ID {category_id} does not exist."
                    }
                ), 400
            product.category_id = category_id

        if 'quantity_id' in data:
            quantity_id = data.get('quantity_id')
            if not QuantityService.get_quantity_by_id(quantity_id):
                return jsonify(
                    {
                        "error": f"Quantity with ID {quantity_id} does not exist."
                    }
                ), 400
            product.quantity_id = quantity_id

        if 'expiration_date' in data:
            product.expiration_date = data.get('expiration_date')

        if 'location_id' in data:
            product.location_id = data.get('location_id')

        # Guardar cambios
        updated_product = ProductService.update_product_instance(product)

        # Serializar esquema
        result = product_schema.dump(updated_product)
        return jsonify(result), 200

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

@product_urls.route('/<int:product_id>', methods=['DELETE'])
@swag_from(delete_product_swagger)
def delete_product(product_id):
    try:
        # Obtener el producto por ID
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Obtener el quantity_id asociado al producto
        quantity_id = product.quantity_id

        # Eliminar el producto
        ProductService.delete_product(product_id)

        # Eliminar registros asociados al quantity_id
        if quantity_id:
            QuantityService.delete_quantity_and_related_data(quantity_id)

        return jsonify({"message": "Product and related data deleted successfully"}), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500
