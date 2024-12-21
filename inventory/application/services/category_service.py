from ...infrastructure.repositories.category_repository import CategoryRepository


class CategoryService():
    @staticmethod
    def create_category(name):
        if not name:
            raise ValueError("Category name can't be empity.")

        return CategoryRepository.create_category(name)

    @staticmethod
    def get_category_by_id(category_id):
        return CategoryRepository.get_category_by_id(category_id)
