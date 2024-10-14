class FinancialRecordException(Exception):
    """Exception raised for errors in financial record management."""
    def __init__(self, message="Error in financial record management."):
        self.message = message
        super().__init__(self.message)
