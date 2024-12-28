from ...infrastructure.repositories.price_repository import PriceRepository


class PriceService():
    @staticmethod
    def create_price(cost_price, sale_price):
        if not (cost_price):
            raise ValueError("Cost price can't be empity.")
        if not (sale_price):
            raise ValueError("Sale price can't be empity.")

        return PriceRepository.create_price(cost_price, sale_price)

    @staticmethod
    def get_all_prices():
        return PriceRepository.get_all_prices()

    @staticmethod
    def get_price_by_id(price_id):
        return PriceRepository.get_price_by_id(price_id)
