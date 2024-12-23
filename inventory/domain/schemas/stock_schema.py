from common.db.db import ma
from ...domain.models.stock import Stock

class StockSchema(ma.Schema):
    class Meta:
        model = Stock
        fields = (
            'id',
            'movement_type',
            'date',
            'quantity_id'
        )

stock_schema = StockSchema()
stock_list_schema = StockSchema(many=True)