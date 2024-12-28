from flask import Blueprint, request

# Swagger
from flasgger import swag_from
from ...application.controllers.stock_controller import *
from ...infrastructure.routes.swagger.stock_swagger import *

stock_urls = Blueprint('stock_blueprint', __name__)

@stock_urls.route('/create', methods=['POST'])
@swag_from(create_stock_swagger)
def create_stock_route():
    data = request.get_json()
    return create_stock(data)

@stock_urls.route('/update_movement_type/<int:stock_id>', methods=['PUT'])
@swag_from(update_movement_type_swagger)
def update_movement_type_route(stock_id):
    data = request.get_json()
    return update_movement_type(stock_id, data)

@stock_urls.route('/all', methods=['GET'])
@swag_from(get_all_stocks_swagger)
def get_all_stocks_route():
    return get_all_stocks()

@stock_urls.route('/<int:stock_id>', methods=['GET'])
@swag_from(get_stock_by_id_swagger)
def get_stock_by_id_route(stock_id):
    return get_stock_by_id(stock_id)

@stock_urls.route('/<int:stock_id>', methods=['DELETE'])
@swag_from(delete_stock_swagger)
def delete_stock_route(stock_id):
    return delete_stock(stock_id)