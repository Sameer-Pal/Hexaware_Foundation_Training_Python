from abc import ABC, abstractmethod
from typing import List, Dict, Any

# IEmployeeService Interface
class IEmployeeService(ABC):
    @abstractmethod
    def get_employee_by_id(self, employee_id: int) -> Dict[str, Any]:
        """Get an employee by their ID."""
        pass

    @abstractmethod
    def get_all_employees(self) -> List[Dict[str, Any]]:
        """Get a list of all employees."""
        pass

    @abstractmethod
    def add_employee(self, employee_data: Dict[str, Any]) -> None:
        """Add a new employee."""
        pass

    @abstractmethod
    def update_employee(self, employee_data: Dict[str, Any]) -> None:
        """Update an existing employee's data."""
        pass

    @abstractmethod
    def remove_employee(self, employee_id: int) -> None:
        """Remove an employee by their ID."""
        pass
