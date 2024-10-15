from abc import ABC, abstractmethod

class AbstractCustomerDAO(ABC):
    
    @abstractmethod
    def insert_customer(self, customer):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass

    @abstractmethod
    def update_customer(self, customer_id, first_name, last_name, email, phone, address):
        pass

    @abstractmethod
    def get_customer_by_id_or_email(self, identifier):
        pass

    @abstractmethod
    def is_valid_email(self, email: str) -> bool:
        pass
