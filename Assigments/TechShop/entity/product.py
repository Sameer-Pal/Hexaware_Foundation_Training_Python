class Product:
    def __init__(self, product_id, product_name, description, price, in_stock=True):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._price = price
        self._in_stock = in_stock

    # Getter and setter for product_id
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        if isinstance(value, int) and value > 0:
            self._product_id = value
        else:
            raise ValueError("Product ID must be a positive integer.")

    # Getter and setter for product_name
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        if value:
            self._product_name = value
        else:
            raise ValueError("Product name cannot be empty.")

    # Getter and setter for description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    # Getter and setter for price with validation
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = value
        else:
            raise ValueError("Price must be a non-negative number.")

    # Getter and setter for in_stock
    @property
    def in_stock(self):
        return self._in_stock

    @in_stock.setter
    def in_stock(self, value):
        if isinstance(value, bool):
            self._in_stock = value
        else:
            raise ValueError("In-stock status must be a boolean.")

    def get_product_details(self):
        return f"Product ID: {self.product_id}, Name: {self.product_name}, Description: {self.description}, Price: ${self.price}, In Stock: {self.in_stock}"

    def update_product_info(self, price=None, description=None):
        if price:
            self.price = price
        if description:
            self.description = description
        print("Product information updated successfully!")

    def is_product_in_stock(self):
        return self.in_stock
