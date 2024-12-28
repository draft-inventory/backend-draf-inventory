from common.db.db import db


class Quantity(db.Model):
    __tablename__ = 'quantity'

    id = db.Column(db.Integer, primary_key=True)
    initial_quantity = db.Column(db.Integer, nullable=False)
    progress_quantity = db.Column(db.Integer, nullable=False)

    # Relación uno a uno con productos
    product = db.relationship(
        'Product', back_populates='quantity', uselist=False)

    # Relación con stocks (uno a uno)
    stocks = db.relationship(
        'Stock', back_populates='quantity', uselist=True)

    # Relación con quantity_history
    history = db.relationship(
        'QuantityHistory', back_populates='quantity', lazy='dynamic')
