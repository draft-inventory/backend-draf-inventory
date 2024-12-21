from ...domain.models.product import Product
from common.db.db import db


class ProductRepository:
    @staticmethod
    def create_product(name, description, product_code, expiration_date, location_id, category_id, quantity_id):
        new_product = Product(
            name=name,
            description=description,
            product_code=product_code,
            expiration_date=expiration_date,
            location_id=location_id,
            category_id=category_id,
            quantity_id=quantity_id
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def product_code_exists(product_code):
        # Consulta para verificar si el product_code ya existe en la base de datos
        return db.session.query(Product).filter_by(product_code=product_code).first() is not None

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.filter_by(id=product_id).first()
