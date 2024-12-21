from common.db.db import ma
from ...domain.models.quantity import Quantity


class QuantitySchema(ma.Schema):
    class Meta:
        model = Quantity
        fields = (
            'id',
            'initial_quantity',
            'progress_quantity'
        )


quantity_schema = QuantitySchema()
quantity_list_schema = QuantitySchema(many=True)
