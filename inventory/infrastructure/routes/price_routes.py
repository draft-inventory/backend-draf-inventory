import re
import traceback
from decimal import Decimal


from flask import Blueprint, request, jsonify
from ...application.services.price_service import PriceService
from ...domain.schemas.price_schema import price_schema, price_list_schema

# Swagger
from flasgger import swag_from
from ...infrastructure.routes.swagger.price_swagger import *

price_urls = Blueprint('price_blueprint', __name__)


@price_urls.route('/create', methods=['POST'])
@swag_from(create_price_swagger)
def create_price():
    try:
        data = request.get_json()
        cost_price = data.get('cost_price')
        sale_price = data.get('sale_price')

        # Validate cost_price
        try:
            cost_price = Decimal(str(cost_price))  # Convert to Decimal
        except (ValueError, TypeError):
            return jsonify(
                {'error': 'Invalid cost_price. It must be a valid number.'}
            ), 400
        if cost_price < 0:
            return jsonify(
                {'error': 'Invalid cost_price. It must be non-negative.'}
            ), 400

        # Validate sale_price
        try:
            sale_price = Decimal(str(sale_price))  # Convert to Decimal
        except (ValueError, TypeError):
            return jsonify(
                {'error': 'Invalid sale_price. It must be a valid number.'}
            ), 400
        if sale_price < 0:
            return jsonify(
                {'error': 'Invalid sale_price. It must be non-negative.'}
            ), 400

        # Additional business rule: sale_price should not be less than cost_price
        if sale_price < cost_price:
            return jsonify(
                {'error': 'Invalid sale_price. It must be greater than or equal to cost_price.'}
            ), 400

        # Create Price

        new_price = PriceService.create_price(cost_price, sale_price)

        # Serialize schema
        result = price_schema.dump(new_price)

        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex), "trace": traceback.format_exc()}), 500


@price_urls.route('/all', methods=['GET'])
@swag_from(get_all_prices_swagger)
def get_all_prices():
    try:
        prices = PriceService.get_all_prices()
        # Asegúrate de usar price_list_schema
        result = price_list_schema.dump(prices)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


@price_urls.route('/<int:price_id>', methods=['GET'])
@swag_from(get_price_by_id_swagger)
def get_price_by_id(price_id):
    try:
        price = PriceService.get_price_by_id(price_id)
        if not price:
            return jsonify({"error": "Price not found"}), 404

        result = price_schema.dump(price)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


@price_urls.route('/<int:price_id>', methods=['PUT'])
@swag_from(update_price_swagger)
def update_price(price_id):
    try:
        data = request.get_json()
        cost_price = data.get('cost_price')
        sale_price = data.get('sale_price')

        # Validaciones (similares al POST)
        try:
            cost_price = Decimal(str(cost_price))
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid cost_price. Must be a valid number."}), 400

        if cost_price < 0:
            return jsonify({"error": "cost_price must be non-negative."}), 400

        try:
            sale_price = Decimal(str(sale_price))
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid sale_price. Must be a valid number."}), 400

        if sale_price < 0:
            return jsonify({"error": "sale_price must be non-negative."}), 400

        if sale_price < cost_price:
            return jsonify({"error": "sale_price must be >= cost_price."}), 400

        updated_price = PriceService.update_price(
            price_id, cost_price, sale_price)
        if not updated_price:
            return jsonify({"error": "Price not found"}), 404

        result = price_schema.dump(updated_price)
        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex), "trace": traceback.format_exc()}), 500
