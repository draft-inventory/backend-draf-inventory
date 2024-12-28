from ...domain.models.price import Price
from common.db.db import db


class PriceRepository():
    @staticmethod
    def create_price(cost_price, sale_price):
        new_price = Price(cost_price=cost_price, sale_price=sale_price)
        db.session.add(new_price)
        db.session.commit()
        return new_price

    @staticmethod
    def get_all_prices():
        return Price.query.all()

    @staticmethod
    def get_price_by_id(price_id):
        return Price.query.get(price_id)

    @staticmethod
    def update_price(price, cost_price, sale_price):
        price.cost_price = cost_price
        price.sale_price = sale_price
        db.session.commit()
        return price

    @staticmethod
    def patch_price(price, fields: dict):
        if 'cost_price' in fields:
            price.cost_price = fields['cost_price']
        if 'sale_price' in fields:
            price.sale_price = fields['sale_price']
        db.session.commit()
        return price

    @staticmethod
    def delete_price(price):
        db.session.delete(price)
        db.session.commit()
        return True
