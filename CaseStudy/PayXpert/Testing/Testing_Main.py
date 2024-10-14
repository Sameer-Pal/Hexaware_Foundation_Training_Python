import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)


import unittest

from dao.Processing.EmployeeService import EmployeeServiceImpl
from dao.Processing.PayrollService import PayrollServiceImpl
from dao.Processing.TaxService import TaxServiceImpl

from util.db_conn_util  import DBUtil

class PayrollService:
    def calculate_gross_salary(self, base_salary, bonuses):
        if base_salary < 0:
            raise ValueError("Base salary cannot be negative")
        return base_salary + bonuses
    def calculate_net_salary(self, gross_salary, deductions):
        return gross_salary - deductions

    def calculate_tax(self, gross_salary):
        if gross_salary > 10000:
            return gross_salary * 0.20  # 20% tax for high income
        return 0

    def process_payroll(self, employees):
        payroll_results = []
        for employee in employees:
            gross_salary = self.calculate_gross_salary(employee.base_salary, employee.bonuses)
            payroll_results.append(gross_salary)
        return payroll_results

class Employee:
    def __init__(self, base_salary, bonuses):
        self.base_salary = base_salary
        self.bonuses = bonuses

class TestPayrollService(unittest.TestCase):
    
    def setUp(self):
        self.payroll_service = PayrollService()

    def test_calculate_gross_salary_valid_input(self):
        # Arrange
        base_salary = 5000
        bonuses = 1000

        # Act
        gross_salary = self.payroll_service.calculate_gross_salary(base_salary, bonuses)

        # Assert
        self.assertEqual(gross_salary, 6000, "The gross salary calculation is incorrect.")

    def test_calculate_net_salary_valid_input(self):
        # Arrange
        gross_salary = 6000
        deductions = 1500  # taxes and insurance

        # Act
        net_salary = self.payroll_service.calculate_net_salary(gross_salary, deductions)

        # Assert
        self.assertEqual(net_salary, 4500, "The net salary calculation after deductions is incorrect.")

    def test_calculate_tax_high_income(self):
        # Arrange
        gross_salary = 20000  # high income
        expected_tax = 4000  # expected tax amount

        # Act
        tax_amount = self.payroll_service.calculate_tax(gross_salary)

        # Assert
        self.assertEqual(tax_amount, expected_tax, "The tax calculation for high-income employee is incorrect.")

    def test_process_payroll_multiple_employees(self):
        # Arrange
        employees = [
            Employee(base_salary=5000, bonuses=1000),
            Employee(base_salary=7000, bonuses=2000),
        ]

        # Act
        payroll_results = self.payroll_service.process_payroll(employees)

        # Assert
        self.assertEqual(payroll_results[0], 6000, "The gross salary for employee 1 is incorrect.")
        self.assertEqual(payroll_results[1], 9000, "The gross salary for employee 2 is incorrect.")

    def test_calculate_gross_salary_invalid_base_salary(self):
        # Arrange
        base_salary = -5000  # invalid base salary
        bonuses = 1000

        # Act & Assert
        with self.assertRaises(ValueError):
            self.payroll_service.calculate_gross_salary(base_salary, bonuses)

if __name__ == '__main__':
    unittest.main()