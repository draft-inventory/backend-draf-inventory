from common.db.db import ma
from ...domain.models.product import Product
from ...domain.schemas.price_schema import PriceSchema


class ProductSchema(ma.Schema):
    # Relación con precio
    price = ma.Nested(PriceSchema)  # Excluye 'product' automáticamente

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'product_code',
            'expiration_date',
            'location_id',
            'category_id',
            'quantity_id',
            'price'
        )


product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True)
