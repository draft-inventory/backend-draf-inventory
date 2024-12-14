from common.db import db
from common.models.base import MVCModel

class Price(MVCModel):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key=True)
    cost_price = db.Column(db.Integer, nullable=False)
    sale_price = db.Column(db.Integer, nullable=False)

    # Relación uno a uno con productos
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship('Product', back_populates='price')