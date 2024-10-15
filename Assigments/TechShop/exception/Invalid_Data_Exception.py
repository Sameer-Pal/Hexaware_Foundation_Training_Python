# exceptions/invalid_data_exception.py

class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided"):
        super().__init__(message)

