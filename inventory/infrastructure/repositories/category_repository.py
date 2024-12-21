from ...domain.models.category import Category
from common.db.db import db


class CategoryRepository():
    @staticmethod
    def create_category(name):
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return new_category

    @staticmethod
    def get_category_by_id(category_id):
        return Category.query.get(category_id)