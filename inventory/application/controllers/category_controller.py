# category_controller.py
import re
from flask import jsonify
from ...application.services.category_service import CategoryService
from ...domain.schemas.category_schema import category_schema, category_list_schema

# Regex para nombres válidos (mueve aquí, para que la lógica viva en el controller)
VALID_NAME_REGEX = r"^[A-Za-zÁÉÍÓÚÑáéíóúñ ]{2,20}$"


def create_category_controller(data):
    """
    Lógica para crear una nueva Category.
    """
    try:
        name = data.get('name')

        # Validate name
        if not name or not re.match(VALID_NAME_REGEX, name):
            return jsonify({
                "error": ("Invalid name. Name must be 2-15 characters, "
                          "no numbers, and only valid Latin characters.")
            }), 400

        # Convertir el nombre a mayúsculas
        name = name.upper()

        # Check if the category name already exists
        if CategoryService.category_name_exists(name):
            return jsonify({
                "error": f"A category with the name '{name}' already exists."
            }), 400

        # Create Category
        new_category = CategoryService.create_category(name)

        # Serializar esquema
        result = category_schema.dump(new_category)
        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def get_category_by_id_controller(category_id):
    """
    Lógica para obtener una Category por ID.
    """
    try:
        category = CategoryService.get_category_by_id(category_id)
        if not category:
            return jsonify({"error": "Category not found"}), 404

        result = category_schema.dump(category)
        return jsonify(result), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def get_all_categories_controller():
    """
    Lógica para obtener todas las Category.
    """
    try:
        categories = CategoryService.get_all_categorys()
        result = category_list_schema.dump(categories)
        return jsonify(result), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def update_category_controller(category_id, data):
    """
    Lógica para actualizar una Category por ID.
    """
    try:
        name = data.get('name')

        # Validate name
        if not name or not re.match(VALID_NAME_REGEX, name):
            return jsonify({
                "error": ("Invalid name. Name must be 2-15 characters, "
                          "no numbers, and only valid Latin characters.")
            }), 400

        # Convertir el nombre a mayúsculas antes de guardar
        name = name.upper()

        updated_category = CategoryService.update_category(category_id, name)
        if not updated_category:
            return jsonify({"error": "Category not found"}), 404

        result = category_schema.dump(updated_category)
        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def patch_category_controller(category_id, fields_to_update):
    """
    Lógica para hacer un PATCH a una Category (actualizar campos específicos).
    """
    try:
        # Validar y convertir el nombre a mayúsculas si está presente
        if "name" in fields_to_update:
            name = fields_to_update.get("name")
            if not name or not re.match(VALID_NAME_REGEX, name):
                return jsonify({
                    "error": ("Invalid name. Name must be 2-15 characters, "
                              "no numbers, and only valid Latin characters.")
                }), 400
            fields_to_update["name"] = name.upper()

        updated_category = CategoryService.patch_category(
            category_id, fields_to_update)
        if not updated_category:
            return jsonify({"error": "Category not found"}), 404

        result = category_schema.dump(updated_category)
        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def delete_category_controller(category_id):
    """
    Lógica para eliminar una Category por ID.
    """
    try:
        deleted_category = CategoryService.delete_category(category_id)
        if not deleted_category:
            return jsonify({"error": "Category not found"}), 404

        return jsonify({"message": "Category deleted successfully"}), 200

    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
