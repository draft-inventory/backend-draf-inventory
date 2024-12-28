from ...infrastructure.repositories.category_repository import CategoryRepository


class CategoryService():
    @staticmethod
    def create_category(name):
        if not name:
            raise ValueError("Category name can't be empity.")

        return CategoryRepository.create_category(name)

    @staticmethod
    def get_category_by_id(category_id):
        category = CategoryRepository.get_category_by_id(category_id)
        if not category:
            raise ValueError(f"Category with ID {category_id} does not exist.")
        return category

    @staticmethod
    def get_all_categorys():
        return CategoryRepository.get_all_categorys()

    @staticmethod
    def update_category(category_id, name):
        # Validate category_id
        category = CategoryRepository.get_category_by_id(category_id)
        if not category:
            raise ValueError(f"Category with ID {category_id} does not exist.")
        return CategoryRepository.update_category(category_id, name)

    @staticmethod
    def patch_category(category_id, fields):
        # Validate category_id
        category = CategoryRepository.get_category_by_id(category_id)
        if not category:
            raise ValueError(f"Category with ID {category_id} does not exist.")
        return CategoryRepository.patch_category(category, fields)

    @ staticmethod
    def delete_category(category_id):
        # Validate category_id
        category = CategoryRepository.get_category_by_id(category_id)

        if not category:
            raise ValueError(f"Category with ID {category_id} does not exist.")
        return CategoryRepository.delete_category(category_id)
