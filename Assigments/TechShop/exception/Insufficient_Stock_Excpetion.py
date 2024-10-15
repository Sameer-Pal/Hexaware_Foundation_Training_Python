# exceptions/insufficient_stock_exception.py
class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock for the product"):

        super().__init__(message)

