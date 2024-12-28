import re
from flask import Blueprint, request
from flasgger import swag_from

# Importa tu nuevo controller
from ...application.controllers.category_controller import *
from ...infrastructure.routes.swagger.category_swagger import *

category_urls = Blueprint('category_blueprint', __name__)


@category_urls.route('/create', methods=['POST'])
@swag_from(create_category_swagger)
def create_category():
    data = request.get_json()
    return create_category_controller(data)  # Delegar al controller


@category_urls.route('/<int:category_id>', methods=['GET'])
@swag_from(get_category_by_id_swagger)
def get_category_by_id(category_id):
    return get_category_by_id_controller(category_id)


@category_urls.route('/all', methods=['GET'])
@swag_from(get_all_categories_swagger)
def get_all_categories():
    return get_all_categories_controller()


@category_urls.route('/<int:category_id>', methods=['PUT'])
@swag_from(update_category_swagger)
def update_category(category_id):
    data = request.get_json()
    return update_category_controller(category_id, data)


@category_urls.route('/<int:category_id>', methods=['PATCH'])
@swag_from(patch_category_swagger)
def patch_category(category_id):
    fields_to_update = request.get_json()
    return patch_category_controller(category_id, fields_to_update)


@category_urls.route('/<int:category_id>', methods=['DELETE'])
@swag_from(delete_category_swagger)
def delete_category(category_id):
    return delete_category_controller(category_id)
