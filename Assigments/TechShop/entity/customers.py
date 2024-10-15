import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)


from exception.Invalid_Data_Exception import InvalidDataException

class Customer:
    def __init__(self, first_name, last_name, email, phone, address, customer_id=None):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._address = address
        self.orders = []  # List to store customer's orders

    # Getter for customer_id
    @property
    def customer_id(self):
        return self._customer_id

    # Setter for customer_id
    @customer_id.setter
    def customer_id(self, value):
        if isinstance(value, int) and value > 0:
            self._customer_id = value
        else:
            raise ValueError("Customer ID must be a positive integer.")

    # Getter and setter for first_name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value:
            self._first_name = value
        else:
            raise ValueError("First name cannot be empty.")

    # Getter and setter for last_name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value:
            self._last_name = value
        else:
            raise ValueError("Last name cannot be empty.")

    # Getter and setter for email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value or '.' not in value:
            raise InvalidDataException("Invalid email address")
        self._email = value
    # Getter and setter for phone
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if value.isdigit() and len(value) == 10:
            self._phone = value
        else:
            raise ValueError("Phone number must be a 10-digit number.")

    # Getter and setter for address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value:
            self._address = value
        else:
            raise ValueError("Address cannot be empty.")

    def calculate_total_orders(self):
        return len(self.orders)

    def get_customer_details(self):
        return f"Customer ID: {self.customer_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Total Orders: {self.calculate_total_orders()}"
      
      # getter for customer's details

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
        print("Customer information updated successfully!")

