from abc import ABC, abstractmethod

class AbstractReportDAO(ABC):
    @abstractmethod
    def generate_sales_report(self):
        """Generates a sales report from the database."""
        pass
