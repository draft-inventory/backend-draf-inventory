from ...infrastructure.repositories.price_repository import PriceRepository

class PriceService():
    @staticmethod
    def create_price(cost_price, sale_price):
        if not (cost_price):
            raise ValueError("Cost price can't be empity.")
        if not (sale_price):
            raise ValueError("Sale price can't be empity.")
        
        return PriceRepository.create_price(cost_price, sale_price)