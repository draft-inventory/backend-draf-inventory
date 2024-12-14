from common.db import db
from common.models.base import MVCModel

class Product(MVCModel):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    product_code = db.Column(db.String(50), unique=True, nullable=False)
    expiration_date = db.Column(db.Date, nullable=True)
    location_id = db.Column(db.String(50), nullable=True)

    # Relación con categoría
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', back_populates='product_list')

    # Relación con cantidad
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantities.id'))
    quantity = db.relationship('Quantity', back_populates='product_list')

    # Relación con precio
    price = db.relationship('Price', back_populates='product', uselist=False)
