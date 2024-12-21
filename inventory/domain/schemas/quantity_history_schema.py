from common.db.db import ma
from ...domain.models.quantity_history import QuantityHistory


class QuantityHistorySchema(ma.Schema):
    class Meta:
        model = QuantityHistory
        fields = (
            'id',
            'quantity_id',
            'date',
            'sold_quantity',
            'remaining_quantity'
        )


quantity_history_schema = QuantityHistorySchema()
quantity_history_list_schema = QuantityHistorySchema(many=True)
