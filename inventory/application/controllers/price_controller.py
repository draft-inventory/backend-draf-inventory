import traceback
from decimal import Decimal
from flask import jsonify
from ...application.services.price_service import PriceService
from ...domain.schemas.price_schema import price_schema, price_list_schema


def create_price_controller(data):
    """
    Lógica para crear un Price.
    """
    try:
        cost_price = data.get('cost_price')
        sale_price = data.get('sale_price')

        # Validar cost_price
        try:
            cost_price = Decimal(str(cost_price))
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid cost_price. Must be a valid number.'}), 400
        if cost_price < 0:
            return jsonify({'error': 'Invalid cost_price. Must be non-negative.'}), 400

        # Validar sale_price
        try:
            sale_price = Decimal(str(sale_price))
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid sale_price. Must be a valid number.'}), 400
        if sale_price < 0:
            return jsonify({'error': 'Invalid sale_price. Must be non-negative.'}), 400

        # Regla de negocio: sale_price >= cost_price
        if sale_price < cost_price:
            return jsonify({'error': 'sale_price must be >= cost_price.'}), 400

        # Crear Price
        new_price = PriceService.create_price(cost_price, sale_price)
        result = price_schema.dump(new_price)
        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({
            "error": "Internal error",
            "except": str(ex),
            "trace": traceback.format_exc()
        }), 500


def get_all_prices_controller():
    """
    Lógica para listar todos los Price.
    """
    try:
        prices = PriceService.get_all_prices()
        result = price_list_schema.dump(prices)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def get_price_by_id_controller(price_id):
    """
    Lógica para obtener un Price por su ID.
    """
    try:
        price = PriceService.get_price_by_id(price_id)
        if not price:
            return jsonify({"error": "Price not found"}), 404

        result = price_schema.dump(price)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500


def update_price_controller(price_id, data):
    """
    Lógica para actualizar un Price.
    """
    try:
        cost_price = data.get('cost_price')
        sale_price = data.get('sale_price')

        # Validaciones (similares a create)
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
        return jsonify({
            "error": "Internal error",
            "except": str(ex),
            "trace": traceback.format_exc()
        }), 500


def patch_price_controller(price_id, fields_to_update):
    """
    Lógica para actualizar un Price con PATCH.
    """
    try:
        updated_price = PriceService.patch_price(price_id, fields_to_update)
        if not updated_price:
            return jsonify({"error": "Price not found"}), 404

        result = price_schema.dump(updated_price)
        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({
            "error": "Internal error",
            "except": str(ex),
            "trace": traceback.format_exc()
        }), 500


def delete_price_controller(price_id):
    """
    Lógica para eliminar un Price.
    """
    try:
        deleted = PriceService.delete_price(price_id)
        if not deleted:
            return jsonify({"error": "Price not found"}), 404
        return jsonify({"message": "Price deleted successfully"}), 200

    except Exception as ex:
        return jsonify({
            "error": "Internal error",
            "except": str(ex),
            "trace": traceback.format_exc()
        }), 500
