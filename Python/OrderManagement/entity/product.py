# 1. Create a base class called Product with the following attributes:
class Product:
    def __init__(self, productName, description, price, quantityInStock, type, productId=None):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

   # 2. Implement constructors, getters, and setters for the Product class.

    # Getters

    def get_product_id(self) -> int:
        return self.productId

    def get_product_name(self) -> str:
        return self.productName

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def get_quantity_in_stock(self) -> int:
        return self.quantityInStock

    def get_type(self) -> str:
        return self.type

    # Setters
    def set_product_name(self, productName: str):
        self.productName = productName

    def set_description(self, description: str):
        self.description = description

    def set_price(self, price: float):
        self.price = price

    def set_quantity_in_stock(self, quantityInStock: int):
        self.quantityInStock = quantityInStock

    def set_type(self, type: str):
        self.type = type

    # Display product details
    def display_product(self):
        print(f"Product ID: {self.productId}")
        print(f"Product Name: {self.productName}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price}")
        print(f"Quantity in Stock: {self.quantityInStock}")
        print(f"Type: {self.type}")
