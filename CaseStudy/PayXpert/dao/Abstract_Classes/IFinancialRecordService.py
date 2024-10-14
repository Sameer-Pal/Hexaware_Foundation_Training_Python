
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class FinancialRecordService(ABC):
    @abstractmethod
    def add_financial_record(self, employee_id: int, description: str, amount: float, record_type: str) -> None:
        """Add a financial record for an employee."""
        pass

    @abstractmethod
    def get_financial_record_by_id(self, record_id: int) -> Dict[str, Any]:
        """Get financial record details by record ID."""
        pass

    @abstractmethod
    def get_financial_records_for_employee(self, employee_id: int) -> List[Dict[str, Any]]:
        """Get all financial records for a specific employee."""
        pass

    @abstractmethod
    def get_financial_records_for_date(self, record_date: str) -> List[Dict[str, Any]]:
        """Get all financial records for a specific date."""
        pass
