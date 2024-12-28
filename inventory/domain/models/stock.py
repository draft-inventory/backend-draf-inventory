from common.db.db import db
from ...domain.models.movement_type import MovementType

class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    movement_type = db.Column(db.Enum(MovementType), nullable=False)  # Usando Enum
    date = db.Column(db.DateTime, nullable=False, default=db.func.now())

    # Relación con quantity (Uno a uno)
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantity.id'), nullable=False)
    quantity = db.relationship('Quantity', back_populates='stocks')
