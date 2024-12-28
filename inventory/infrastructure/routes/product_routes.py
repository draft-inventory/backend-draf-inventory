import re
from flask import Blueprint, request
from flasgger import swag_from

from ...application.controllers.product_controller import *
from ...infrastructure.routes.swagger.product_swagger import *

product_urls = Blueprint('product_blueprint', __name__)


@product_urls.route('/create', methods=['POST'])
@swag_from(create_product_swagger)
def create_product():
    data = request.get_json()
    return create_product_controller(data)


@product_urls.route('/all', methods=['GET'])
@swag_from(get_all_products_swagger)
def get_all_products():
    return get_all_products_controller()


@product_urls.route('/<int:product_id>', methods=['GET'])
@swag_from(get_product_by_id_swagger)
def get_product_by_id(product_id):
    return get_product_by_id_controller(product_id)


@product_urls.route('/<int:product_id>', methods=['PUT'])
@swag_from(update_product_swagger)
def update_product(product_id):
    data = request.get_json()
    return update_product_controller(product_id, data)


@product_urls.route('/<int:product_id>', methods=['PATCH'])
@swag_from(patch_product_swagger)
def patch_product(product_id):
    data = request.get_json()
    return patch_product_controller(product_id, data)


@product_urls.route('/<int:product_id>', methods=['DELETE'])
@swag_from(delete_product_swagger)
def delete_product(product_id):
    return delete_product_controller(product_id)
