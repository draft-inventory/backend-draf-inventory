from ...infrastructure.repositories.product_repository import ProductRepository


class ProductService:
    @staticmethod
    def create_product(name, description, product_code, expiration_date, location_id, category_id, quantity_id):
        return ProductRepository.create_product(name, description, product_code, expiration_date, location_id, category_id, quantity_id)
