from ...infrastructure.repositories.quantity_repository import QuantityRepository
from ...infrastructure.repositories.quantity_history_repository import QuantityHistoryRepository


class QuantityService():
    @staticmethod
    def create_quantity(initial_quantity, progress_quantity):
        # Validar initial_quantity
        if initial_quantity < 0:
            raise ValueError("Initial quantity can't be negative.")

        # Validar progress_quantity
        if progress_quantity < 0:
            raise ValueError("Progress quantity can't be negative.")

        # Validar relación entre initial_quantity y progress_quantity
        if initial_quantity < progress_quantity:
            raise ValueError(
                "Initial quantity must be greater than or equal to progress quantity.")

        # Delegar la creación al repositorio
        return QuantityRepository.create_quantity(initial_quantity, progress_quantity)

    @staticmethod
    def get_quantity_by_id(quantity_id):
        # Implementar método de recuperación desde el repositorio
        return QuantityRepository.get_quantity_by_id(quantity_id)

    @staticmethod
    def update_progress_quantity(quantity_id, new_progress_quantity):
        # Implementar método de actualización desde el repositorio
        return QuantityRepository.update_progress_quantity(quantity_id, new_progress_quantity)

    @staticmethod
    def get_all_quantities():
        return QuantityRepository.get_all_quantities()

    @staticmethod
    def update_quantity(quantity_id, initial_quantity, progress_quantity):
        if initial_quantity < 0 or progress_quantity < 0:
            raise ValueError("Quantities can't be negative.")
        if initial_quantity < progress_quantity:
            raise ValueError(
                "Initial quantity must be greater than or equal to progress quantity.")
        return QuantityRepository.update_quantity(quantity_id, initial_quantity, progress_quantity)

    @staticmethod
    def delete_quantity(quantity_id):
        # Eliminar todas las referencias en quantity_history
        QuantityHistoryRepository.delete_by_quantity_id(quantity_id)
        return QuantityRepository.delete_quantity(quantity_id)

    @staticmethod
    def patch_quantity(quantity_id, fields_to_update):
        if "initial_quantity" in fields_to_update and fields_to_update["initial_quantity"] < 0:
            raise ValueError("Initial quantity can't be negative.")
        if "progress_quantity" in fields_to_update and fields_to_update["progress_quantity"] < 0:
            raise ValueError("Progress quantity can't be negative.")
        if "initial_quantity" in fields_to_update and "progress_quantity" in fields_to_update:
            if fields_to_update["initial_quantity"] < fields_to_update["progress_quantity"]:
                raise ValueError(
                    "Initial quantity must be greater than or equal to progress quantity.")
        return QuantityRepository.patch_quantity(quantity_id, fields_to_update)

    @staticmethod
    def delete_quantity_and_related_data(quantity_id):
        # Eliminar registros relacionados en QuantityHistory
        QuantityHistoryRepository.delete_by_quantity_id(quantity_id)

        # Eliminar el registro principal en Quantity
        quantity = QuantityRepository.get_quantity_by_id(quantity_id)
        if quantity:
            QuantityRepository.delete_quantity(quantity_id)
            return {"message": f"Quantity ID {quantity_id} and related history deleted successfully"}
        else:
            return {"error": f"Quantity ID {quantity_id} not found"}
