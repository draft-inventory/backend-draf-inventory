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

    @staticmethod
    def get_all_quantity_histories():
        return QuantityHistory.query.all()

    @staticmethod
    def get_quantity_history_by_id(quantity_history_id):
        return QuantityHistory.query.filter_by(id=quantity_history_id).first()

    @staticmethod
    def get_quantity_history_by_quantity_id(quantity_id):
        return QuantityHistory.query.filter_by(quantity_id=quantity_id).all()

    @staticmethod
    def delete_by_quantity_id(quantity_id):
        QuantityHistory.query.filter_by(quantity_id=quantity_id).delete()
        db.session.commit()

    @staticmethod
    def delete_quantity_history(quantity_history_id):
        quantity_history = QuantityHistory.query.get(quantity_history_id)
        if quantity_history:
            db.session.delete(quantity_history)
            db.session.commit()
        return quantity_history
