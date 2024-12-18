from common.db.db import db


class Price(db.Model):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key=True)
    cost_price = db.Column(db.Integer, nullable=False)
    sale_price = db.Column(db.Integer, nullable=False)

    # Relación uno a uno con productos
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship('Product', back_populates='price')