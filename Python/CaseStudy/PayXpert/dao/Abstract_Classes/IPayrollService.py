from abc import ABC, abstractmethod
from typing import List, Dict, Any

# IPayrollService Interface
class PayrollService(ABC):
    @abstractmethod
    def generate_payroll(self, employee_id: int, start_date: str, end_date: str) -> None:
        """Generate payroll for an employee for a specific period."""
        pass

    @abstractmethod
    def get_payroll_by_payrolId(self, payroll_id: int) -> Dict[str, Any]:
        """Get payroll details by payroll ID."""
        pass

    @abstractmethod
    def get_payrolls_for_employeeID(self, employee_id: int) -> List[Dict[str, Any]]:
        """Get all payroll records for a specific employee."""
        pass

    @abstractmethod
    def get_payrolls_for_period(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """Get all payroll records for a specific period."""
        pass