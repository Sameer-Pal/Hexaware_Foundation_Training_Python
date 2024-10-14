from abc import ABC, abstractmethod
from typing import List, Dict, Any

# ITaxService Interface
class TaxService(ABC):
    @abstractmethod
    def calculate_tax(self, employee_id: int, tax_year: int) -> float:
        """Calculate tax for an employee for a specific year."""
        pass

    @abstractmethod
    def get_tax_by_id(self, tax_id: int) -> Dict[str, Any]:
        """Get tax details by tax ID."""
        pass

    @abstractmethod
    def get_taxes_for_employee(self, employee_id: int) -> List[Dict[str, Any]]:
        """Get all tax records for a specific employee."""
        pass

    @abstractmethod
    def get_taxes_for_year(self, tax_year: int) -> List[Dict[str, Any]]:
        """Get all tax records for a specific year."""
        pass
