from abc import ABC, abstractmethod
from entity.product import Product

class AbstractProductDAO(ABC):
    @abstractmethod
    def insert_product(self, product: Product) -> None:
        """Inserts a new product into the database."""
        pass

    @abstractmethod
    def update_product(self, product: Product) -> None:
        """Updates an existing product in the database."""
        pass

    @abstractmethod
    def get_all_products(self):
        """Retrieves all products from the database."""
        pass

    @abstractmethod
    def search_and_recommendations(self, product_name: str, category: str):
        """Searches for products and provides recommendations based on category."""
        pass

    @abstractmethod
    def remove_product(self, product_id: int) -> None:
        """Removes a product from the database."""
        pass
