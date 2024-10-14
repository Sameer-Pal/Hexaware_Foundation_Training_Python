
class TaxCalculationException(Exception):
    """Exception raised for errors in tax calculation."""
    def __init__(self, message="Error calculating taxes for the employee."):
        self.message = message
        super().__init__(self.message)
