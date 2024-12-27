from flask import Blueprint, request, jsonify
from ...application.services.stock_service import StockService
from ...application.services.quantity_service import QuantityService
from ...domain.schemas.stock_schema import stock_schema, stock_list_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.routes.swagger.stock_swagger import *

stock_urls = Blueprint('stock_blueprint', __name__)

@stock_urls.route('/create', methods=['POST'])
@swag_from(create_stock_swagger)
def create_stock():
    try:
        data = request.get_json()
        movement_type = data.get('movement_type')
        quantity_id = data.get('quantity_id')

        # Validate input
        if not movement_type or quantity_id is None:
            return jsonify({"error": "Invalid movement_type name or quantity_id."}), 400
        
        # Validar existencia de quantity_id
        if not QuantityService.get_quantity_by_id(quantity_id):
             return jsonify({"error": f"Quantity with ID {quantity_id} does not exist."}), 400

        # Create Stock
        new_stock = StockService.create_stock(movement_type, quantity_id)

        # Serialize schema
        result = stock_schema.dump(new_stock)

        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500

@stock_urls.route('/update_movement_type/<int:stock_id>', methods=['PUT'])
@swag_from(update_movement_type_swagger)
def update_movement_type(stock_id):
    try:
        data = request.get_json()
        movement_type = data.get('movement_type')

        # Validate input
        if not movement_type:
            return jsonify({"error": "Missing movement type."}), 400

        # Update movement type
        updated_stock = StockService.update_movement_type(stock_id, movement_type)

        # Serialize schema
        result = stock_schema.dump(updated_stock)

        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500

@stock_urls.route('/all', methods=['GET'])
@swag_from(get_all_stocks_swagger)
def get_all_stocks():
    try:
        stocks = StockService.get_all_stocks()
        result = stock_list_schema.dump(stocks)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify(
            {"error": "Internal error", "exception": str(ex)}
        ), 500


@stock_urls.route('/<int:stock_id>', methods=['GET'])
@swag_from(get_stock_by_id_swagger)
def get_stock_by_id(stock_id):
    try:
        stock = StockService.get_stock_by_id(stock_id)
        if not stock:
            return jsonify({"error": "Stock not found"}), 404
        result = stock_schema.dump(stock)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500

@stock_urls.route('/<int:stock_id>', methods=['DELETE'])
@swag_from(delete_stock_swagger)
def delete_stock(stock_id):
    try:
        deleted_stock = StockService.delete_stock(stock_id)
        if not deleted_stock:
            return jsonify({"error": "Stock not found"}), 404
        return jsonify({"message": "Stock deleted successfully"}), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500