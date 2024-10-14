class EmployeeNotFoundException(Exception):
    """Exception raised when an employee is not found."""
    def __init__(self, message="Employee not found."):
        self.message = message
        super().__init__(self.message)