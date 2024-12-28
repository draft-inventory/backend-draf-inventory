import traceback
from decimal import Decimal
from flask import Blueprint, request
from flasgger import swag_from

from ...application.controllers.price_controller import *
from ...infrastructure.routes.swagger.price_swagger import *

price_urls = Blueprint('price_blueprint', __name__)


@price_urls.route('/create', methods=['POST'])
@swag_from(create_price_swagger)
def create_price():
    data = request.get_json()
    return create_price_controller(data)


@price_urls.route('/all', methods=['GET'])
@swag_from(get_all_prices_swagger)
def get_all_prices():
    return get_all_prices_controller()


@price_urls.route('/<int:price_id>', methods=['GET'])
@swag_from(get_price_by_id_swagger)
def get_price_by_id(price_id):
    return get_price_by_id_controller(price_id)


@price_urls.route('/<int:price_id>', methods=['PUT'])
@swag_from(update_price_swagger)
def update_price(price_id):
    data = request.get_json()
    return update_price_controller(price_id, data)


@price_urls.route('/<int:price_id>', methods=['PATCH'])
@swag_from(patch_price_swagger)
def patch_price(price_id):
    fields_to_update = request.get_json()
    return patch_price_controller(price_id, fields_to_update)


@price_urls.route('/<int:price_id>', methods=['DELETE'])
@swag_from(delete_price_swagger)
def delete_price(price_id):
    return delete_price_controller(price_id)
