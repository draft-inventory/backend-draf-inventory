from flask import Blueprint, request

# Swagger
from flasgger import swag_from

from ...application.controllers.quantity_history_controller import *
from ...infrastructure.routes.swagger.quantity_history_swagger import *

quantity_history_urls = Blueprint('quantity_history_blueprint', __name__)


@quantity_history_urls.route('/create', methods=['POST'])
@swag_from(create_quantity_history_swagger)
def create_quantity_history_route():
    data = request.get_json()
    return create_quantity_history(data)

@quantity_history_urls.route('/all', methods=['GET'])
@swag_from(get_all_quantity_histories_swagger)
def get_all_quantity_histories_route():
    return get_all_quantity_histories()


@quantity_history_urls.route('/<int:quantity_history_id>', methods=['GET'])
@swag_from(get_quantity_history_by_id_swagger)
def get_quantity_history_by_id_route(quantity_history_id):
    return get_quantity_history_by_id(quantity_history_id)

@quantity_history_urls.route('/quantity/<int:quantity_id>', methods=['GET'])
@swag_from(get_quantity_by_quiantity_id_swagger)
def get_quantity_by_quiantity_id_route(quantity_id):
    return get_quantity_by_quantity_id(quantity_id)

@quantity_history_urls.route('/<int:quantity_history_id>', methods=['DELETE'])
@swag_from(delete_quantity_history_swagger)
def delete_quantity_history_route(quantity_history_id):
    return delete_quantity_history(quantity_history_id)


@quantity_history_urls.route('/<int:quantity_history_id>', methods=['PUT'])
@swag_from(update_quantity_history_swagger)
def update_quantity_history_route(quantity_history_id):
    data = request.get_json()
    return update_quantity_history(quantity_history_id, data)

@quantity_history_urls.route('/<int:quantity_history_id>', methods=['PATCH'])
@swag_from(patch_quantity_history_swagger)
def patch_quantity_history_route(quantity_history_id):
    data = request.get_json()
    return patch_quantity_history(quantity_history_id, data)