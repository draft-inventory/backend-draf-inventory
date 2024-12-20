from common.db.db import ma
from ...domain.models.price import Price

class PriceSchema(ma.Schema):
    class Meta:
        model = Price
        fields = (
            'id',
            'cost_price',
            'sale_price'
        )

price_schema = PriceSchema()
price_list_schema = PriceSchema(many=True)