from common.db.db import db

class QuantityHistory(db.Model):
    __tablename__ = 'quantity_history'

    id = db.Column(db.Integer, primary_key=True)
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantity.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    sold_quantity = db.Column(db.Integer, nullable=False)
    remaining_quantity = db.Column(db.Integer, nullable=False)

    # Relación inversa con Quantity
    quantity = db.relationship('Quantity', back_populates='history')
