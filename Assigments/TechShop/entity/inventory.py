from datetime import datetime
from entity.product import Product
from exception.Invalid_Data_Exception import InvalidDataException
from exception.Insufficient_Stock_Excpetion import  InsufficientStockException

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock):
        self._inventory_id = inventory_id
        self.product = product  # Composition: Reference to Product
        self._quantity_in_stock = quantity_in_stock
        self._last_stock_update = datetime.now()
        self._products = []  # Private list to hold the products in the inventory

    # Getter for products
    @property
    def products(self):
        return self._products

    # Getter and setter for inventory_id
    @property
    def inventory_id(self):
        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, value):
        if isinstance(value, int) and value > 0:
            self._inventory_id = value
        else:
            raise ValueError("Inventory ID must be a positive integer.")




    # Getter and setter for product
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, Product):
            self._product = value
        else:
            raise ValueError("Invalid product.")

    # Getter

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        self.quantity_in_stock += quantity
        self.last_stock_update = datetime.now()
        print(f"Added {quantity} to inventory. Total in stock: {self.quantity_in_stock}")

    def remove_from_inventory(self, quantity):
        if quantity <= self.quantity_in_stock:
            self.quantity_in_stock -= quantity
            self.last_stock_update = datetime.now()
            print(f"Removed {quantity} from inventory. Total in stock: {self.quantity_in_stock}")
        else:
            raise InsufficientStockException(f"Not enough stock for {self.product.product_name}. Requested: {quantity}, Available: {self._quantity_in_stock}")

    def update_stock_quantity(self, new_quantity):
        self.quantity_in_stock = new_quantity
        self.last_stock_update = datetime.now()
        print(f"Stock quantity updated to {self.quantity_in_stock}")

    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.product.price * self.quantity_in_stock

    def list_low_stock_products(self, threshold):
        if self.quantity_in_stock < threshold:
            return f"{self.product.product_name} is low in stock with {self.quantity_in_stock} left."
        return f"{self.product.product_name} has sufficient stock."

    def list_out_of_stock_products(self):
        if self.quantity_in_stock == 0:
            return f"{self.product.product_name} is out of stock."
        return f"{self.product.product_name} is in stock."

    def list_all_products(self):
        return f"Product: {self.product.product_name}, Quantity in Stock: {self.quantity_in_stock}"


    # Method to add a product to the inventory
    def add_product(self, product, quantity):
        if isinstance(product, Product) and isinstance(quantity, int) and quantity > 0:
            self._products.append({"product": product, "quantity": quantity})
        else:
            raise ValueError("Invalid product or quantity. Quantity must be a positive integer.")

 # Method to remove a product from the inventory
    def remove_product(self, product_id):
        for item in self._products:
            if item["product"].product_id == product_id:
                self._products.remove(item)
                return True
        raise ValueError(f"Product with ID {product_id} not found in inventory.")

    # Method to update the quantity of a product in the inventory
    def update_quantity(self, product_id, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        
        for item in self._products:
            if item["product"].product_id == product_id:
                item["quantity"] = quantity
                return True
        raise ValueError(f"Product with ID {product_id} not found in inventory.")

    # Method to check if a product is available in the inventory
    def is_product_available(self, product_id):
        for item in self._products:
            if item["product"].product_id == product_id and item["quantity"] > 0:
                return True
        return False

    # Method to get the inventory details
    def get_inventory_details(self):
        details = []
        for item in self._products:
            product_info = item["product"].get_product_details()
            details.append(f"{product_info}, Quantity: {item['quantity']}")
        return "\n".join(details)
