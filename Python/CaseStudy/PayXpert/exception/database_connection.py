class DatabaseConnectionException(Exception):
    """Exception raised for database connection errors."""
    def __init__(self, message="Unable to connect to the database."):
        self.message = message
        super().__init__(self.message)
