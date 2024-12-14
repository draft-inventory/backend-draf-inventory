from common.db import db
from common.models.base import MVCModel

class Quantity(MVCModel):
    __tablename__ = 'quantities'

    id = db.Column(db.Integer, primary_key=True)
    initial_quantity = db.Column(db.Integer, nullable=False)
    progress_quantity = db.Column(db.Integer, nullable=False)

    # Relación con productos
    product_list = db.relationship('Product', back_populates='quantity')

    # Relación con stock
    stock = db.relationship('Stock', back_populates='quantity', uselist=False)
