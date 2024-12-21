from ...infrastructure.repositories.quantity_repository import QuantityRepository

class QuantityService():
    @staticmethod
    def create_quantity(initial_quantity, progress_quantity):
        if initial_quantity < 0:
            raise ValueError("Initial quantity can't be negative.")
        if progress_quantity < 0:
            raise ValueError("Progress quantity can't be negative.")

        return QuantityRepository.create_quantity(initial_quantity, progress_quantity)
