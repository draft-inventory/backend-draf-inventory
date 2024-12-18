from common.db.db import db


class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    movement_type = db.Column(db.String(50), nullable=False)  # Ej: entrada, salida, ajuste
    date = db.Column(db.DateTime, nullable=False, default=db.func.now())

    # Relación con cantidad
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantities.id'))
    quantity = db.relationship('Quantity', back_populates='stock')
