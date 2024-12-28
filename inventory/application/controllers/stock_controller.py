from flask import jsonify
from ...application.services.stock_service import StockService
from ...application.services.quantity_service import QuantityService
from ...domain.schemas.stock_schema import stock_schema, stock_list_schema

def create_stock(data):
    """
    Lógica para crear un Stock.
    """
    try:
        movement_type = data.get('movement_type')
        quantity_id = data.get('quantity_id')
        
        # Validar movement_type
        if not movement_type or quantity_id is None:
            return jsonify({"error": "Invalid movement_type name or quantity_id."}), 400
        
        # Validar existencia de quantity_id
        if not QuantityService.get_quantity_by_id(quantity_id):
             return jsonify({"error": f"Quantity with ID {quantity_id} does not exist."}), 400

        # Crear Stock en la base de datos
        new_stock = StockService.create_stock(movement_type, quantity_id)

        # Serializar resultado
        result = stock_schema.dump(new_stock)

        return jsonify(result), 201

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
    
def get_all_stocks():
    """
    Lógica para listar todos los Stock.
    """
    try:
        stocks = StockService.get_all_stocks()
        result = stock_list_schema.dump(stocks)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
    
def get_stock_by_id(stock_id):
    """
    Lógica para obtener un Stock por su ID.
    """
    try:
        stock = StockService.get_stock_by_id(stock_id)
        if not stock:
            return jsonify({"error": "Stock not found"}), 404
        result = stock_schema.dump(stock)
        return jsonify(result), 200
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
    
def update_movement_type(stock_id, data):
    """
    Lógica para actualizar el movimiento de un Stock.
    """
    try:
        movement_type = data.get('movement_type')

        # Validar movement_type
        if not movement_type:
            return jsonify({"error": "Missing movement type."}), 400

        # Actualizar movimiento
        updated_stock = StockService.update_movement_type(stock_id, movement_type)

        # Serializar resultado
        result = stock_schema.dump(updated_stock)

        return jsonify(result), 200

    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500
    
def delete_stock(stock_id):
    """
    Lógica para eliminar un Stock.
    """
    try:
        result = StockService.delete_stock(stock_id)
        return jsonify(result), 200
    except ValueError as ex:
        return jsonify({"error": str(ex)}), 400
    except Exception as ex:
        return jsonify({"error": "Internal error", "except": str(ex)}), 500