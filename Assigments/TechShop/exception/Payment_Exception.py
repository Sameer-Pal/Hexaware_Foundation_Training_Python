

# exceptions/payment_failed_exception.py
class PaymentFailedException(Exception):
    def __init__(self, message="Payment failed"):
        super().__init__(message)

