from ...domain.models.stock import Stock
from common.db.db import db


class StockRepository:
    @staticmethod
    def create_stock(movement_type, quantity_id):
        new_stock = Stock(
            movement_type=movement_type,
            quantity_id=quantity_id
        )
        db.session.add(new_stock)
        db.session.commit()
        return new_stock

    @staticmethod
    def get_all_stocks():
        return Stock.query.all()

    @staticmethod
    def get_stock_by_id(stock_id):
        return Stock.query.get(stock_id)
    
    #TODO: Ask how this is used and update, if not used, delete. 
    @staticmethod
    def update_movement_type(stock_id, movement_type):
        stock = Stock.query.get(stock_id)
        if stock:
            stock.movement_type = movement_type
            db.session.commit()
        return stock
    
    @staticmethod
    def delete_stock(stock_id):
        stock = Stock.query.get(stock_id)
        if stock:
            db.session.delete(stock)
            db.session.commit()
        return stock
    
    #TODO: Ask how patch_stock works ;-;