from abc import ABC, abstractmethod

class AbstractOrderDAO(ABC):
    @abstractmethod
    def place_order(self, order):
        pass

    @abstractmethod
    def get_order_status(self, order_id):
        pass

    @abstractmethod
    def update_order_status(self, order_id, new_status):
        pass

    @abstractmethod
    def remove_canceled_orders(self):
        pass

    @abstractmethod
    def retrieve_orders(self):
        pass

    @abstractmethod
    def sort_orders_by_date(self, ascending=True):
        pass

    @abstractmethod
    def get_orders_by_date_range(self, start_date, end_date):
        pass
