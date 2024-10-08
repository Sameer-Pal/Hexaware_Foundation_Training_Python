# 3. Create a subclass Electronics that inherits from Product
from entity.product import Product


class Electronics(Product):
    def __init__(self, productName, description, price, quantityInStock, brand, model, warranty, power_usage):
        super().__init__(self, productName, description, price,
                         quantityInStock, "Electronics")  # Call the base class constructor
        self.brand = brand  # Brand of the electronic product
        self.warranty = warranty  # Warranty period (in months or years)

    # Getters
    def getBrand(self):
        return self.brand

    def getWarrantyPeriod(self):
        return self.warrantyPeriod

    # Setters
    def setBrand(self, brand):
        self.brand = brand

    def setWarrantyPeriod(self, warrantyPeriod):
        self.warrantyPeriod = warrantyPeriod
