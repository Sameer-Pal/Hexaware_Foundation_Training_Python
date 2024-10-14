import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)


from datetime import datetime

from dao.Processing.PayrollService import PayrollServiceImpl
from dao.Processing.TaxService import TaxServiceImpl
from dao.Processing.EmployeeService import EmployeeServiceImpl
from dao.Processing.FinancialRecordService import FinancialRecordServiceImpl
from entity.validation_service import ValidationService
class MainModule:
    def __init__(self):
        self.employee_service = EmployeeServiceImpl()
        self.payroll_service = PayrollServiceImpl()
        self.tax_service = TaxServiceImpl()
        self.financial_record_service = FinancialRecordServiceImpl()
        self.validation_Service = ValidationService

    def display_menu(self):
        print("\n--- Payroll Management System ---")
        print("1. Employee Management")
        print("2. Payroll Processing")
        print("3. Tax Calculation")
        print("4. Financial Reporting")
        print("5. Exit")
   

    def main_menu(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            
            if choice == '1':
                self.employee_management()
            elif choice == '2':
                self.payroll_processing()
            elif choice == '3':
                self.tax_calculation()
            elif choice == '4':
                self.financial_calculation()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")
     
    #  EMPLOYEE
    def employee_management_menu(self):
        print("\n--- Employee Management ---")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. Get Employee by ID")
        print("5. View All Employees")
        print("6. Back to Main Menu")



    def employee_management(self):
        while True:
            self.employee_management_menu()
            choice = input("Select an option: ")

            if choice == '1':
                # Call the add employee method from employee_service
                self.add_employee()
            elif choice == '2':
                self.update_employee()
            elif choice == '3':
                self.remove_employee()
            elif choice == '4':
                self.get_employee_by_id()
            elif choice == '5':
                self.get_all_employees()
            elif choice == '6':
                break
            else:
                print("Invalid option. Please try again.")

    def add_employee(self):
        """Gather employee data and add a new employee."""
        employee_data = {
         'first_name': input("Enter first name: "),
         'last_name': input("Enter last name: "),
         'date_of_birth': input("Enter date of birth (YYYY-MM-DD): "),
         'gender': input("Enter gender: "),
         'email': input("Enter email: "),
         'phone_number': input("Enter phone number: "),

         'address': input("Enter address: "),
         'position': input("Enter position: "),
         'joining_date': input("Enter joining date (YYYY-MM-DD): ")
                        }
        

        phone_number = employee_data['phone_number']
        if not phone_number.isdigit() or len(phone_number) != 10:
          print("Error: Phone number must be exactly 10 digits and numeric.")
          return
        # Add other employee details + phone number validatoin
        
        self.employee_service.add_employee(employee_data)
        print("Employee added successfully!")

    def get_employee_by_id(self):
        employee_id = int(input("Enter Employee ID: "))
        employee = self.employee_service.get_employee_by_id(employee_id)
        print(f"Employee details: {employee}")

    def get_all_employees(self):
     """Get and display all employees."""
     employees = self.employee_service.get_all_employees()
     if employees:
        print("\nList of All Employees:")
        for employee in employees:
            print(f"Employee ID: {employee['employee_id']}")
            print(f"Name: {employee['first_name']} {employee['last_name']}")
            print(f"Position: {employee['position']}")
            print(f"Email: {employee['email']}")
            print(f"Phone: {employee['phone_number']}")
            print(f"Address: {employee['address']}")
            print(f"Joining Date: {employee['joining_date']}")
            print(f"Termination Date: {employee['termination_date']}")
            print()
     else:
        print("No employees found.")


    def update_employee(self):
     """Update an employee's information."""
     try:
        employee_id = int(input("Enter Employee ID to update: "))
        employee_data = self.employee_service.get_employee_by_id(employee_id)
        
        if employee_data:
            print(f"Updating information for {employee_data['first_name']} {employee_data['last_name']}")
            
            employee_data['first_name'] = input(f"First Name [{employee_data['first_name']}]: ") or employee_data['first_name']
            employee_data['last_name'] = input(f"Last Name [{employee_data['last_name']}]: ") or employee_data['last_name']
            employee_data['email'] = input(f"Email [{employee_data['email']}]: ") or employee_data['email']
            employee_data['phone_number'] = input(f"Phone [{employee_data['phone_number']}]: ") or employee_data['phone_number']
            employee_data['address'] = input(f"Address [{employee_data['address']}]: ") or employee_data['address']
            employee_data['position'] = input(f"Position [{employee_data['position']}]: ") or employee_data['position']
            employee_data['termination_date'] = input(f"Termination Date [{employee_data['termination_date']}]: ") or employee_data['termination_date']

            phone_number = employee_data['phone_number']
            if not phone_number.isdigit() or len(phone_number) != 10:
                print("Error: Phone number must be exactly 10 digits and numeric.")
                return
            # Call the update method from employee_service
            self.employee_service.update_employee(employee_data)
            print("Employee updated successfully!")
        else:
            print(f"Employee with ID {employee_id} not found.")
     except ValueError:
        print("Invalid Employee ID entered.")



    def remove_employee(self):
     """Remove an employee by their ID."""
     try:
        employee_id = int(input("Enter Employee ID to remove: "))
        
        confirmation = input(f"Are you sure you want to remove Employee ID {employee_id}? (y/n): ").lower()
        
        if confirmation == 'y':
            self.employee_service.remove_employee(employee_id)
            print(f"Employee ID {employee_id} has been removed.")
        else:
            print("Operation cancelled.")
            
     except ValueError:
        print("Invalid Employee ID entered.")




    # PAYROLL
    
    def payroll_processing_menu(self):
        print("\n--- Payroll Processing ---")
        print("1. Generate Payroll")
        print("2. Get Payroll by Payroll ID")
        print("3. Get Payrolls for Employee")
        print("4. Get Payrolls for period ")
        print("5. Back to Main Menu")


    def payroll_processing(self):
        while True:
            self.payroll_processing_menu()
            choice = input("Select an option: ")

 
            if choice == '1':
                employee_id = int(input("Enter Employee ID: "))
                start_date = datetime.strptime(input("Enter starting date (YYYY-MM-DD): "), '%Y-%m-%d')

                end_date = datetime.strptime(input("Enter ending date (YYYY-MM-DD): "),'%Y-%m-%d')
                self.generate_payroll(employee_id,start_date,end_date)
            elif choice == '2':
                # Get Payroll by ID
                payroll_id = int(input("Enter Payroll ID: "))
                self.get_payroll_by_payrolId(payroll_id)
            elif choice == '3':
                # Get Payrolls for Employee
                employee_id = int(input("Enter Employee ID: "))
                self.get_payrolls_for_employeeId(employee_id)
            elif choice == '4':
                # Get Payrolls for a Period
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                self.get_payrolls_for_period(start_date, end_date)
            elif choice == '5':
                break  # Exit the payroll processing menu
            else:
                print("Invalid option. Please try again.")

                   
    def generate_payroll(self, employee_id: int, start_date, end_date):
     result = self.payroll_service.generate_payroll(employee_id, start_date, end_date)
     if result:
        print(f"Payroll generated successfully.",result)
     else:
        print("Failed to generate payroll.")


    def get_payroll_by_payrolId(self, payroll_id: int):
        payroll = self.payroll_service.get_payroll_by_payrolId(payroll_id)
        if payroll:
            print(f"Payroll Details: {payroll}")
        else:
            print("Payroll not found.")

    def get_payrolls_for_employeeId(self, employee_id: int):
        payrolls = self.payroll_service.get_payrolls_for_employeeID(employee_id)
        if payrolls:
            for payroll in payrolls:
                print(f"Payroll ID: {payroll['payroll_id']}, Amount: {payroll['net_salary']}")
        else:
            print("No payrolls found for this employee.")

    def get_payrolls_for_period(self, start_date: str, end_date: str):
        payrolls = self.payroll_service.get_payrolls_for_period(start_date, end_date)
        if payrolls:
            for payroll in payrolls:
                print(f"Payroll ID: {payroll['payroll_id']}, Employee ID: {payroll['employee_id']}, Amount: {payroll['net_salary']}")
        else:
            print("No payrolls found for this period.")


    # TAX
    def tax_calculation_menu(self):
        """Print the tax calculation menu options."""
        print("\nTax Calculation Menu:")
        print("1. Calculate Tax for Employee")
        print("2. Get Tax By ID")
        print("3. Get Taxes for Employee")
        print("4. Get Taxes for Year")
        print("5. Exit")

 

    def tax_calculation(self):
        """Handle tax calculation options."""
        while True:
            self.tax_calculation_menu()  # Print the menu options
            choice = input("Select an option: ")

            if choice == '1':
             try:
              employee_id = int(input("Enter Employee ID: "))
              tax_year = int(input("Enter Tax Year: "))
              self.tax_service.calculate_tax(employee_id, tax_year)
            #   print(f"Calculated Tax: {tax:.2f}")  # Print the tax amount
             except ValueError as e:
              print(f"Invalid input: {e}") 
            elif choice == '2':
                tax_id = int(input("Enter Tax ID: "))
                tax_details = self.tax_service.get_tax_by_id(tax_id)
                print(f"Tax Details: {tax_details}")
            
            elif choice == '3':
                employee_id = int(input("Enter Employee ID: "))
                taxes = self.tax_service.get_taxes_for_employee(employee_id)
                print(f"Taxes for Employee ID {employee_id}: {taxes}")
            
            elif choice == '4':
                tax_year = int(input("Enter Tax Year: "))
                taxes = self.tax_service.get_taxes_for_year(tax_year)
                if taxes:
                 print(f"Taxes for Year {tax_year}: {taxes}\n")
                else:
                    print("No Data is Present")
            
            elif choice == '5':
                print("Exiting the tax calculation menu.")
                break
            
            else:
                print("Invalid option. Please try again.")





# FINANCIAL REPORTING 

    def financial_calc_menu(self):
        """Display the menu options for financial records."""
        print("\nFinancial Record Menu:")
        print("1. Add Financial Record")
        print("2. Get Financial Record By ID")
        print("3. Get Financial Records For Employee")
        print("4. Get Financial Records For Date")
        print("5. Exit")


    def financial_calculation(self):
        """Handle the menu interaction."""
        while True:
            self.financial_calc_menu()
            choice = input("Select an option: ")

            if choice == '1':
                employee_id = int(input("Enter Employee ID: "))
                description = input("Enter Description: ")
                amount = float(input("Enter Amount: "))
                record_type = input("Enter Record Type (Income/Expense): ")
                self.financial_record_service.add_financial_record(employee_id, description, amount, record_type)           
            elif choice == '2':
                record_id = int(input("Enter Record ID: "))
                record = self.financial_record_service.get_financial_record_by_id(record_id)
                print(f"Financial Record: {record}")
            elif choice == '3':
                employee_id = int(input("Enter Employee ID: "))
                records = self.financial_record_service.get_financial_records_for_employee(employee_id)
                print(f"Financial Records for Employee ID {employee_id}: {records}")
            elif choice == '4':
                record_date = input("Enter Record Date (YYYY-MM-DD): ")
                records = self.financial_record_service.get_financial_records_for_date(record_date)
                if records:print(f"Financial Records for Date {record_date}: {records}")
                else:
                    print("no data is present")
            elif choice == '5':
                print("Exiting the financial record menu.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = MainModule()
    app.main_menu()