from abc import ABC, abstractmethod
from decimal import Decimal

class AbstractPaymentDAO(ABC):
    @abstractmethod
    def record_payment(self, order_id: int, payment_method: str, amount: Decimal) -> bool:
        """Records the payment details for an order."""
        pass

