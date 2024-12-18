from common.db.db import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relación con productos
    # product_list = db.relationship('Product', back_populates='category')