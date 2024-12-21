from ...infrastructure.repositories.quantity_history_repository import QuantityHistoryRepository


class QuantityHistoryService():
    @staticmethod
    def create_quantity_history(quantity_id, date, sold_quantity, remaining_quantity):
        if not quantity_id:
            raise ValueError("Quantity id can't be empity.")
        if not date:
            raise ValueError("Date can't be empity.")
        if sold_quantity < 0:
            raise ValueError("Sold quantity can't be negative.")
        if remaining_quantity < 0:
            raise ValueError("Remaining quantity can't be negative.")

        return QuantityHistoryRepository.create_quantity_history(quantity_id, date, sold_quantity, remaining_quantity)

    @staticmethod
    def get_all_quantity_histories():
        return QuantityHistoryRepository.get_all_quantity_histories()

    @staticmethod
    def get_quantity_history_by_id(quantity_id):
        return QuantityHistoryRepository.get_quantity_history_by_id(quantity_id)

    @staticmethod
    def get_quantity_history_by_quantity_id(quantity_id):
        return QuantityHistoryRepository.get_quantity_history_by_quantity_id(quantity_id)

    @staticmethod
    def delete_by_quantity_id(quantity_id):
        return QuantityHistoryRepository.delete_by_quantity_id(quantity_id)
