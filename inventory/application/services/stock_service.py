from ...infrastructure.repositories.stock_repository import StockRepository
from ...infrastructure.repositories.quantity_repository import QuantityRepository
from ...domain.models.movement_type import MovementType

class StockService():
    @staticmethod
    def create_stock(movement_type, quantity_id):
        # Validar movement_type
        if movement_type not in MovementType.__members__:
            raise ValueError(f"Invalid movement_type. Must be one of {list(MovementType.__members__.keys())}")

        # Validar quantity_id
        quantity = QuantityRepository.get_quantity_by_id(quantity_id)
        if not quantity:
            raise ValueError(f"Quantity with ID {quantity_id} does not exist.")

        # Delegar la creación al repositorio
        return StockRepository.create_stock(movement_type, quantity_id)

    @staticmethod
    def get_all_stocks():
        return StockRepository.get_all_stocks()

    @staticmethod
    def get_stock_by_id(stock_id):
        # Validar stock_id
        stock = StockRepository.get_stock_by_id(stock_id)
        if not stock:
            raise ValueError(f"Stock with ID {stock_id} does not exist.")
        return stock

    @staticmethod
    def update_movement_type(stock_id, movement_type):
        # Validar movement_type
        if movement_type not in MovementType.__members__:
            raise ValueError(f"Invalid movement_type. Must be one of {list(MovementType.__members__.keys())}")

        # Validar stock_id y actualizar
        stock = StockRepository.get_stock_by_id(stock_id)
        if not stock:
            raise ValueError(f"Stock with ID {stock_id} does not exist.")

        return StockRepository.update_movement_type(stock_id, movement_type)

    @staticmethod
    def delete_stock(stock_id):
        # Validar stock_id
        stock = StockRepository.get_stock_by_id(stock_id)
        if not stock:
            raise ValueError(f"Stock with ID {stock_id} does not exist.")

        return StockRepository.delete_stock(stock_id)