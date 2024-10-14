
class InvalidInputException(Exception):
    """Exception raised for invalid input data."""
    def __init__(self, message="Invalid input data provided."):
        self.message = message
        super().__init__(self.message)
