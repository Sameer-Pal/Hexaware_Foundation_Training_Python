# exceptions/incomplete_order_exception.py
class IncompleteOrderException(Exception):
    def __init__(self, message="Incomplete order details"):
        super().__init__(message)

