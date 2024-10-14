from typing import List, Dict, Any
from util.db_conn_util import DBUtil
from dao.Abstract_Classes.ITaxService import  TaxService
from decimal import Decimal


class TaxServiceImpl(TaxService):
    def __init__(self):
        self.connection = DBUtil.getDBConn()
    def calculate_tax(self, employee_id: int, tax_year: int) -> Decimal:
        """Calculate tax for an employee for a specific year."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT BasicSalary FROM Payroll WHERE EmployeeID = ?"
            cursor.execute(query, (employee_id,))
            salary = cursor.fetchone()
            
            if not salary:
                raise ValueError(f"No employee found with ID {employee_id}.")
                
            # Convert salary to Decimal
            basic_salary = Decimal(salary[0])  # Access the first element of the tuple and convert to Decimal

            # A simple tax calculation logic (replace with actual logic)
            tax_rate = Decimal('0.15')  # Use Decimal for tax rate
            
            # Calculate tax
            tax = basic_salary * tax_rate
            print(f"Calculated Tax: {tax:.2f}")  # Print with two decimal places
       
        except Exception as e:
            print(f"Failed to calculate tax: {e}")
            return Decimal('0.0')  # Return Decimal zero if there's an error
        finally:
            cursor.close()

    def get_tax_by_id(self, tax_id: int) -> Dict[str, Any]:
        """Get tax details by tax ID."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Tax WHERE TaxID = ?"
            cursor.execute(query, (tax_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "tax_id": row[0],  # Adjust indexing according to your DB schema
                    "employee_id": row[1],
                    "tax_year": row[2],
                    "amount": row[3]
                }
            else:
                raise ValueError(f"Tax record with ID {tax_id} not found.")
        except Exception as e:
            print(f"Failed to fetch tax: {e}")
            return {}
        finally:
            cursor.close()

    def get_taxes_for_employee(self, employee_id: int) -> List[Dict[str, Any]]:
        """Get all tax records for a specific employee."""
        taxes = []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Tax WHERE EmployeeID = ?"
            cursor.execute(query, (employee_id,))
            rows = cursor.fetchall()
           
            for row in rows:
                taxes.append({
                    "tax_id": row[0],
                    "employee_id": row[1],
                    "tax_year": row[2],
                    "amount": row[3]
                })
            if len(taxes)==0: 
                print("No Data is Present") 
                return 
            else: return taxes
        except Exception as e:
            print(f"Failed to fetch taxes for employee: {e}")
            return []
        finally:
            cursor.close()

    def get_taxes_for_year(self, tax_year: int) -> List[Dict[str, Any]]:
        """Get all tax records for a specific year."""
        taxes = []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Tax WHERE TaxYear = ?"
            cursor.execute(query, (tax_year,))
            rows = cursor.fetchall()
            for row in rows:
                taxes.append({
                    "tax_id": row[0],
                    "employee_id": row[1],
                    "tax_year": row[2],
                    "amount": row[3]
                })
            if len(taxes)==0:
                print("Not Present")    
                return
            else:    
                return taxes
        except Exception as e:
            print(f"Failed to fetch taxes for year: {e}")
            return []
        finally:
            cursor.close()