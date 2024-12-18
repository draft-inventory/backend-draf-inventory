from common.db.db import ma
from ...domain.models.category import Category


class CategorySchema(ma.Schema):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


category_schema = CategorySchema()
category_list_schema = CategorySchema(many=True)
