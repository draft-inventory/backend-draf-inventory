from common.db.db import db
from ...domain.models.movement_type import MovementType

class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    movement_type = db.Column(db.Enum(MovementType), nullable=False)  # Using Enum
    date = db.Column(db.DateTime, nullable=False, default=db.func.now())

    # Relación con cantidad
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantities.id'), nullable=False)
    quantity = db.relationship('Quantity', back_populates='stock')
