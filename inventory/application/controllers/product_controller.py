import re
from flask import jsonify
from ...application.services.quantity_service import QuantityService
from ...application.services.category_service import CategoryService
from ...application.services.product_service import ProductService
from ...domain.schemas.product_schema import product_schema, product_list_schema

# Patrón para validar 'name' (solo letras y espacios)
NAME_REGEX = r"^[A-Za-z\s]+$"
# Patrón para validar 'description' (caracteres alfanuméricos y espacios)
DESCRIPTION_REGEX = r"^[A-Za-z0-9\s]+$"


def create_product_controller(data):
    """
    Lógica para crear un producto.
    """
    try:
        name = data.get('name')
        description = data.get('description')
        category_id = data.get('category_id')
        quantity_id = data.get('quantity_id')

        # Validar campo name
        if not re.match(NAME_REGEX, name):
            return jsonify({"error": "Name must only contain alphabetic characters and spaces."}), 400

        # Validar campo description
        if not re.match(DESCRIPTION_REGEX, description):
            return jsonify({"error": "Description must only contain alphanumeric characters and spaces."}), 400

        # Validar existencia de category_id
        if not CategoryService.get_category_by_id(category_id):
            return jsonify({"error": f"Category with ID {category_id} does not exist."}), 400

        # Validar existencia de quantity_id
        if not QuantityService.get_quantity_by_id(quantity_id):
            return jsonify({"error": f"Quantity with ID {quantity_id} does not exist."}), 400

        # Generar product_code
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
        result = product_schema.dump(new_product)
        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def get_all_products_controller():
    """
    Lógica para obtener todos los productos.
    """
    try:
        products = ProductService.get_all_products()
        result = product_list_schema.dump(products)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500


def get_product_by_id_controller(product_id):
    """
    Lógica para obtener un producto por ID.
    """
    try:
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        result = product_schema.dump(product)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500


def update_product_controller(product_id, data):
    """
    Lógica para actualizar un producto.
    """
    try:
        name = data.get('name')
        description = data.get('description')
        category_id = data.get('category_id')
        quantity_id = data.get('quantity_id')

        # Validar campo name
        if not re.match(NAME_REGEX, name):
            return jsonify({"error": "Name must only contain alphabetic characters and spaces."}), 400

        # Validar campo description
        if not re.match(DESCRIPTION_REGEX, description):
            return jsonify({"error": "Description must only contain alphanumeric characters and spaces."}), 400

        # Validar existencia de category_id
        if not CategoryService.get_category_by_id(category_id):
            return jsonify({"error": f"Category with ID {category_id} does not exist."}), 400

        # Validar existencia de quantity_id
        if not QuantityService.get_quantity_by_id(quantity_id):
            return jsonify({"error": f"Quantity with ID {quantity_id} does not exist."}), 400

        # Generar product_code
        product_code_base = f"{name[0].upper()}{name[-1].upper()}"
        product_code = product_code_base
        counter = 1
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

        result = product_schema.dump(updated_product)
        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500


def patch_product_controller(product_id, data):
    """
    Lógica para hacer un PATCH a un producto.
    """
    try:
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Actualizar campos según los presentes en `data`
        if 'name' in data:
            name = data['name']
            if not re.match(NAME_REGEX, name):
                return jsonify({"error": "Name must only contain alphabetic characters and spaces."}), 400

            product.name = name
            # Actualizar product_code
            product_code_base = f"{name[0].upper()}{name[-1].upper()}"
            product_code = product_code_base
            counter = 1
            while ProductService.check_product_code_exists(product_code):
                product_code = f"{product_code_base}_{counter}"
                counter += 1
            product.product_code = product_code

        if 'description' in data:
            description = data['description']
            if not re.match(DESCRIPTION_REGEX, description):
                return jsonify({"error": "Description must only contain alphanumeric characters and spaces."}), 400
            product.description = description

        if 'category_id' in data:
            category_id = data['category_id']
            if not CategoryService.get_category_by_id(category_id):
                return jsonify({"error": f"Category with ID {category_id} does not exist."}), 400
            product.category_id = category_id

        if 'quantity_id' in data:
            quantity_id = data['quantity_id']
            if not QuantityService.get_quantity_by_id(quantity_id):
                return jsonify({"error": f"Quantity with ID {quantity_id} does not exist."}), 400
            product.quantity_id = quantity_id

        if 'expiration_date' in data:
            product.expiration_date = data['expiration_date']

        if 'location_id' in data:
            product.location_id = data['location_id']

        # Guardar cambios
        updated_product = ProductService.patch_product(product)
        result = product_schema.dump(updated_product)
        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "exception": str(ex)}), 500


def delete_product_controller(product_id):
    """
    Lógica para eliminar un producto (y sus datos relacionados).
    """
    try:
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
