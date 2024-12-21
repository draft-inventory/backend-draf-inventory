from ...infrastructure.repositories.quantity_repository import QuantityRepository


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
