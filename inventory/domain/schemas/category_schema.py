from domain.models.category import Category
from common.db import db

class CategorySchema(db.Schema):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )
    
category_schema = CategorySchema()
category_list_schema = CategorySchema(many = True)