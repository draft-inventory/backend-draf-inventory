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
    def dump(self, obj, **kwargs):
     # Convertir `movement_type` a una cadena
     if obj.movement_type:
         obj.movement_type = obj.movement_type.name
     return super().dump(obj, **kwargs)
        
stock_schema = StockSchema()
stock_list_schema = StockSchema(many=True)