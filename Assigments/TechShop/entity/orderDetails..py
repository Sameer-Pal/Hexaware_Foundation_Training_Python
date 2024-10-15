from product import Product
from order import Order
from exception.Incomplete_Order_Exception import IncompleteOrderException
class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self._order_detail_id = order_detail_id
        self._order = order
        self._product = product
        self._quantity = quantity
        self._discount = 0
        self._subtotal = self.calculate_subtotal()  # Calculate subtotal during initialization


    # Getter and setter for order_detail_id
    @property
    def order_detail_id(self):
        return self._order_detail_id

    @order_detail_id.setter
    def order_detail_id(self, value):
        if isinstance(value, int) and value > 0:
            self._order_detail_id = value
        else:
            raise ValueError("Order Detail ID must be a positive integer.")

    # Getter and setter for order
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        if isinstance(value, Order):
            self._order = value
        else:
            raise ValueError("Invalid order. Must be an Orders object.")

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

    # Getter and setter for quantity with validation
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int) and value > 0:
            self._quantity = value
            self._subtotal = self.calculate_subtotal()  # Recalculate subtotal if quantity changes

        else:
            raise ValueError("Quantity must be a positive integer.")

    # Getter and setter for discount with validation
    @property
    def discount(self):
        return self._discount
    def validate_order_detail(self):
        if self.product is None:
            raise IncompleteOrderException("Order detail is missing a product reference.")


    @discount.setter
    def discount(self, value):
        if isinstance(value, (int, float)) and 0 <= value <= 100:
            self._discount = value
        else:
            raise ValueError("Discount must be between 0 and 100.")

    def calculate_subtotal(self):
        return (self.product.price * self.quantity) - self.discount
    
    def get_order_detail_info(self):
        return f"Order Detail ID: {self._order_detail_id}, Product: {self._product.product_name}, " \
               f"Quantity: {self._quantity}, Subtotal: {self._subtotal}"
 
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Quantity updated.")
 
    def add_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            discount_amount = (self._subtotal * discount_percentage) / 100
            self._subtotal -= discount_amount
        else:
            raise ValueError("Discount percentage must be between 0 and 100.")