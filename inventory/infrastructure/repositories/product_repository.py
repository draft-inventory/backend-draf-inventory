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

    @staticmethod
    def get_by_quantity_id(quantity_id):
        return Product.query.filter_by(quantity_id=quantity_id).first()

    @staticmethod
    def update_product(product_id, name, description, product_code, expiration_date, location_id, category_id, quantity_id):
        product = Product.query.filter_by(id=product_id).first()
        if product:
            product.name = name
            product.description = description
            product.product_code = product_code
            product.expiration_date = expiration_date
            product.location_id = location_id
            product.category_id = category_id
            product.quantity_id = quantity_id
            db.session.commit()
        return product

    @staticmethod
    def patch_product(product_instance):
        db.session.commit()
        return product_instance

    @staticmethod
    def delete_product(product_id):
        product = Product.query.filter_by(id=product_id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
        return product
