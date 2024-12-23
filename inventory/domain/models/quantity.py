from common.db.db import db


class Quantity(db.Model):
    __tablename__ = 'quantity'

    id = db.Column(db.Integer, primary_key=True)
    initial_quantity = db.Column(db.Integer, nullable=False)
    progress_quantity = db.Column(db.Integer, nullable=False)

    # Relación con productos
    products = db.relationship(
        'Product', back_populates='quantity')

    # Relación con stocks
    stocks = db.relationship(
        'Stock', back_populates='quantity', lazy='dynamic')

    # Relación con quantity_history
    history = db.relationship(
        'QuantityHistory', back_populates='quantity', lazy='dynamic')
