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
    def category_name_exists(name):
        return db.session.query(Category).filter_by(name=name).first() is not None

    @staticmethod
    def get_category_by_id(category_id):
        return Category.query.get(category_id)

    @staticmethod
    def get_all_categorys():
        return Category.query.all()

    @staticmethod
    def update_category(category_id, name):
        category = Category.query.get(category_id)
        if category:
            category.name = name
            db.session.commit()
        return category

    @staticmethod
    def patch_category(category, fields):
        for key, value in fields.items():
            setattr(category, key, value)
        db.session.commit()
        return category

    @staticmethod
    def delete_category(category_id):
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
        return category
