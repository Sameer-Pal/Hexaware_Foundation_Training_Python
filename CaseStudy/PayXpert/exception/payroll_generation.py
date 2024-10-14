class PayrollGenerationException(Exception):
    """Exception raised for errors in payroll generation."""
    def __init__(self, message="Error generating payroll for the employee."):
        self.message = message
        super().__init__(self.message)
  
    def payroll_doesnt_exist(self,message="payrollID does not exist"):
        self.message=message
        super().__init__(self.message)