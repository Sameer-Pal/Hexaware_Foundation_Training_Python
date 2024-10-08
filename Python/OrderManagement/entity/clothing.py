# 4. Create a subclass Clothing that also inherits from Product.

from entity.product import Product


class Clothing(Product):

    def __init__(self, productName, description, price, quantityInStock, size, color):
        super().__init__(self, productName, description, price, quantityInStock, "Clothing")
        self.size = size  # Size of the clothing item (e.g., S, M, L, XL)
        # Color of the clothing item (e.g., Red, Blue, Black)
        self.color = color

    # Getters
    def getSize(self):
        return self.size

    def getColor(self):
        return self.color

    # Setters
    def setSize(self, size):
        self.size = size

    def setColor(self, color):
        self.color = color
