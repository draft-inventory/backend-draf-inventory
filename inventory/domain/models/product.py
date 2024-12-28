from common.db.db import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    product_code = db.Column(db.String(50), unique=True, nullable=False)
    expiration_date = db.Column(db.Date, nullable=True)
    location_id = db.Column(db.String(50), nullable=True)

    # Relación con categoría
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=True)
    category = db.relationship('Category', back_populates='product_list')

    # Relación uno a uno con cantidad
    quantity_id = db.Column(db.Integer, db.ForeignKey(
        'quantity.id'), unique=True, nullable=True)
    quantity = db.relationship(
        'Quantity', back_populates='product', uselist=False)

    # Relación con precio (uno a uno)
    price = db.relationship('Price', back_populates='product', uselist=False)
