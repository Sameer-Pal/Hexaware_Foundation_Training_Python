import re
from decimal import Decimal
from datetime import datetime

class ValidationService:
    @staticmethod
    def validate_employee_data(employee_data):
        """
        Validates the employee data.
        :param employee_data: A tuple containing employee details.
        :raises ValueError: If any validation rule fails.
        """
        first_name, last_name, date_of_birth, gender, email, phone_number, address, position, joining_date = employee_data
        
        # Validate first name and last name
        if not first_name or not last_name:
            raise ValueError("First name and last name are required.")
        
        # Validate date of birth format and value
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date of birth must be a valid date in YYYY-MM-DD format.")
        
        # Validate gender (only allow 'M' or 'F')
        if gender not in ('M', 'F'):
            raise ValueError("Gender must be either 'M' or 'F'.")
        
        # Validate email address format
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid email address.")
        
        # Validate phone number (10 to 15 digits, can start with a '+')
        if not re.match(r"^\+?[0-9\s\-]{10,15}$", phone_number):
            raise ValueError("Invalid phone number.")
        
        # Validate position (must not be empty)
        if not position:
            raise ValueError("Position is required.")
        
        # Validate joining date format and value
        try:
            datetime.strptime(joining_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Joining date must be a valid date in YYYY-MM-DD format.")
        
    @staticmethod
    def validate_salary_data(basic_salary, overtime_pay, deductions):
        """
        Validates the payroll salary data.
        :param basic_salary: The basic salary of the employee.
        :param overtime_pay: The overtime pay for the employee.
        :param deductions: The total deductions for the employee.
        :raises ValueError: If any validation rule fails.
        """
        # Validate basic salary (must be a positive number)
        if not isinstance(basic_salary, (float, Decimal)) or basic_salary < 0:
            raise ValueError("Basic salary must be a positive number.")
        
        # Validate overtime pay (must be a positive number)
        if not isinstance(overtime_pay, (float, Decimal)) or overtime_pay < 0:
            raise ValueError("Overtime pay must be a positive number.")
        
        # Validate deductions (must be a positive number)
        if not isinstance(deductions, (float, Decimal)) or deductions < 0:
            raise ValueError("Deductions must be a positive number.")
