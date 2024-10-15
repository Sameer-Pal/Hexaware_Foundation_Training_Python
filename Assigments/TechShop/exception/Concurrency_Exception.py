# exceptions/concurrency_exception.py
class ConcurrencyException(Exception):
    def __init__(self, message="Data conflict detected. The data has been modified by another user."):
        self.message = message
        super().__init__(self.message)
