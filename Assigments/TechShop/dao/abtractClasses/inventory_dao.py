from abc import ABC, abstractmethod

class AbstractInventoryDAO(ABC):
    
    @abstractmethod
    def add_product(self, product_id, quantity):
        pass

    @abstractmethod
    def update_inventory(self, product_id, quantity):
        pass

    @abstractmethod
    def delete_inventory_product(self, inventory_id):
        pass

    @abstractmethod
    def get_all_inventory(self):
        pass
