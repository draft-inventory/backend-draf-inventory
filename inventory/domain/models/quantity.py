from common.db.db import db


class Quantity(db.Model):
    __tablename__ = 'quantities'

    id = db.Column(db.Integer, primary_key=True)
    initial_quantity = db.Column(db.Integer, nullable=False)
    progress_quantity = db.Column(db.Integer, nullable=False)

    # Relación con productos
    product_list = db.relationship('Product', back_populates='quantity')

    # Relación con stock
    stock = db.relationship('Stock', back_populates='quantity', uselist=False)
