from ...infrastructure.repositories.product_repository import ProductRepository


class ProductService:
    @staticmethod
    def create_product(name, description, product_code, expiration_date, location_id, category_id, quantity_id):
        # Validar que el quantity_id no esté ya asociado a otro Product
        if quantity_id:
            existing_product = ProductRepository.get_by_quantity_id(
                quantity_id)
            if existing_product:
                raise ValueError(
                    f"Quantity ID {quantity_id} is already associated with another product.")

        return ProductRepository.create_product(
            name, description, product_code, expiration_date, location_id, category_id, quantity_id
        )

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
        # Validar que el quantity_id no esté ya asociado a otro Product
        if quantity_id:
            existing_product = ProductRepository.get_by_quantity_id(
                quantity_id)
            if existing_product and existing_product.id != product_id:
                raise ValueError(
                    f"Quantity ID {quantity_id} is already associated with another product.")

        return ProductRepository.update_product(
            product_id, name, description, product_code, expiration_date, location_id, category_id, quantity_id
        )

    @staticmethod
    def patch_product(product_id, fields):
        # Validar que el quantity_id no esté ya asociado a otro Product
        quantity_id = fields.get('quantity_id')
        if quantity_id:
            existing_product = ProductRepository.get_by_quantity_id(
                quantity_id)
            if existing_product and existing_product.id != product_id:
                raise ValueError(
                    f"Quantity ID {quantity_id} is already associated with another product.")

        product = ProductRepository.get_product_by_id(product_id)

        if not product:
            return None

        return ProductRepository.patch_product(product, fields)

    @staticmethod
    def delete_product(product_id):
        return ProductRepository.delete_product(product_id)
