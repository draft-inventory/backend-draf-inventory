from ...infrastructure.repositories.product_repository import ProductRepository


class ProductService:
    @staticmethod
    def create_product(name, description, product_code, expiration_date, location_id, category_id, quantity_id):
        return ProductRepository.create_product(name, description, product_code, expiration_date, location_id, category_id, quantity_id)

    @staticmethod
    def check_product_code_exists(product_code):
        # Llama al repositorio para verificar si el product_code ya existe
        return ProductRepository.product_code_exists(product_code)

    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def update_product(product_id, name, description, product_code, expiration_date, location_id, category_id, quantity_id):
        return ProductRepository.update_product(
            product_id, name, description, product_code, expiration_date, location_id, category_id, quantity_id
        )

    @staticmethod
    def update_product_instance(product_instance):
        return ProductRepository.update_product_instance(product_instance)

    @staticmethod
    def delete_product(product_id):
        return ProductRepository.delete_product(product_id)
