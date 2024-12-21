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
