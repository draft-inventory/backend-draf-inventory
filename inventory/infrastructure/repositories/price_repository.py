from ...domain.models.price import Price
from common.db.db import db

class PriceRepository():
    @staticmethod
    def create_price(cost_price, sale_price):
        new_price = Price(cost_price=cost_price, sale_price=sale_price)
        db.session.add(new_price)
        db.session.commit()
        return new_price