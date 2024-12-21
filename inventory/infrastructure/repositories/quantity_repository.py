from ...domain.models.quantity import Quantity
from common.db.db import db


class QuantityRepository:
    @staticmethod
    def create_quantity(initial_quantity, progress_quantity):
        new_quantity = Quantity(
            initial_quantity=initial_quantity,
            progress_quantity=progress_quantity
        )
        db.session.add(new_quantity)
        db.session.commit()
        return new_quantity

    @staticmethod
    def get_quantity_by_id(quantity_id):
        return Quantity.query.get(quantity_id)

    @staticmethod
    def update_progress_quantity(quantity_id, new_progress_quantity):
        quantity = Quantity.query.get(quantity_id)
        if quantity:
            quantity.progress_quantity = new_progress_quantity
            db.session.commit()
        return quantity

    @staticmethod
    def get_all_quantities():
        return Quantity.query.all()
