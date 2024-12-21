from ...domain.models.quantity_history import QuantityHistory
from common.db.db import db


class QuantityHistoryRepository():
    @staticmethod
    def create_quantity_history(quantity_id, date, sold_quantity, remaining_quantity):
        new_quantity_history = QuantityHistory(
            quantity_id=quantity_id, date=date, sold_quantity=sold_quantity, remaining_quantity=remaining_quantity)
        db.session.add(new_quantity_history)
        db.session.commit()
        return new_quantity_history
