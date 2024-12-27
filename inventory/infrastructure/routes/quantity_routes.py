from flask import Blueprint, request
from flasgger import swag_from

from ...application.controllers.quantity_controller import *
from ...infrastructure.routes.swagger.quantity_swagger import *

quantity_urls = Blueprint('quantity_blueprint', __name__)


@quantity_urls.route('/create', methods=['POST'])
@swag_from(create_quantity_swagger)
def create_quantity_route():
    data = request.get_json()
    return create_quantity(data)


@quantity_urls.route('/all', methods=['GET'])
@swag_from(get_all_quantities_swagger)
def get_all_quantities_route():
    return get_all_quantities()


@quantity_urls.route('/<int:quantity_id>', methods=['GET'])
@swag_from(get_quantity_by_id_swagger)
def get_quantity_by_id_route(quantity_id):
    return get_quantity_by_id(quantity_id)


@quantity_urls.route('/<int:quantity_id>', methods=['PUT'])
@swag_from(update_quantity_swagger)
def update_quantity_route(quantity_id):
    data = request.get_json()
    return update_quantity(quantity_id, data)


@quantity_urls.route('/<int:quantity_id>', methods=['DELETE'])
@swag_from(delete_quantity_swagger)
def delete_quantity_route(quantity_id):
    return delete_quantity(quantity_id)


@quantity_urls.route('/<int:quantity_id>', methods=['PATCH'])
@swag_from(patch_quantity_swagger)
def patch_quantity_route(quantity_id):
    fields_to_update = request.get_json()
    return patch_quantity(quantity_id, fields_to_update)
