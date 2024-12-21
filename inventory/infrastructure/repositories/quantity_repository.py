from ...domain.models.quantity import Quantity
from common.db.db import db


class QuantityRepository():
    @staticmethod
    def create_quantity(initial_quantity, progress_quantity):
        new_quantity = Quantity(
            initial_quantity=initial_quantity, progress_quantity=progress_quantity)
        db.session.add(new_quantity)
        db.session.commit()
        return new_quantity
