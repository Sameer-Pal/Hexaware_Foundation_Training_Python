from typing import List, Dict, Any
from util.db_conn_util import DBUtil
from dao.Abstract_Classes.IEmployeeService import IEmployeeService

class EmployeeServiceImpl(IEmployeeService):
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def get_employee_by_id(self, employee_id: int) -> Dict[str, Any]:
     """Fetch employee data by employee ID."""
     try:
        cursor = self.connection.cursor()
        query = "SELECT * FROM Employee WHERE EmployeeID = ?"
        cursor.execute(query, (employee_id,))
        row = cursor.fetchone()

        if row:
            employee_data = {
                'employee_id': row[0],         # EmployeeID
                'first_name': row[1],          # FirstName
                'last_name': row[2],           # LastName
                'date_of_birth': row[3],       # DateOfBirth
                'gender': row[4],              # Gender
                'email': row[5],               # Email
                'phone_number': row[6],        # PhoneNumber
                'address': row[7],             # Address
                'position': row[8],            # Position
                'joining_date': row[9],        # JoiningDate
                'termination_date': row[10]
            }
            return employee_data
        
        return None 
     except Exception as e:
        print(f"Failed to fetch employee: {e}")
        return None
     finally:
        cursor.close()

    def get_all_employees(self) -> List[Dict[str, Any]]:
        """Get a list of all employees."""
        employees = []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Employee"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                employees.append({
                    "employee_id": row.EmployeeID,
                    "first_name": row.FirstName,
                    "last_name": row.LastName,
                    "date_of_birth": row.DateOfBirth,
                    "gender": row.Gender,
                    "email": row.Email,
                    "phone_number": row.PhoneNumber,
                    "address": row.Address,
                    "position": row.Position,
                    "joining_date": row.JoiningDate,
                    "termination_date": row.TerminationDate
                })
            return employees
        except Exception as e:
            print(f"Failed to fetch all employees: {e}")
            return []
        finally:
            cursor.close()

    def add_employee(self, employee_data: Dict[str, Any]) -> None:
        """Add a new employee."""
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                employee_data['first_name'],
                employee_data['last_name'],
                employee_data['date_of_birth'],
                employee_data['gender'],
                employee_data['email'],
                employee_data['phone_number'],
                employee_data['address'],
                employee_data['position'],
                employee_data['joining_date']
            ))
            cursor.connection.commit()  # Commit changes
            print("Employee added successfully.")
        except Exception as e:
            print(f"Failed to add employee: {e}")
        finally:
            cursor.close()  # Close the cursor
    def update_employee(self, employee_data: Dict[str, Any]) -> None:
        """Update an existing employee's data."""
        try:
            cursor = self.connection.cursor()
            query = """
                UPDATE Employee
                SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Email = ?, PhoneNumber = ?, Address = ?, Position = ?, JoiningDate = ?, TerminationDate = ?
                WHERE EmployeeID = ?
            """
            cursor.execute(query, (
                employee_data['first_name'],
                employee_data['last_name'],
                employee_data['date_of_birth'],
                employee_data['gender'],
                employee_data['email'],
                employee_data['phone_number'],
                employee_data['address'],
                employee_data['position'],
                employee_data['joining_date'],
                employee_data.get('termination_date'),  # This can be None if not applicable
                employee_data['employee_id']
            ))
            self.connection.commit()
            print("Employee updated successfully.")
        except Exception as e:
            print(f"Failed to update employee: {e}")
        finally:
            cursor.close()

    def employee_exists(self, employee_id: int) -> bool:
     """Check if an employee exists in the database."""
     try:
        cursor = self.connection.cursor()
        query = "SELECT 1 FROM Employee WHERE EmployeeID = ?"
        cursor.execute(query, (employee_id,))
        result = cursor.fetchone()
        
        # If a result is found, the employee exists
        return result is not None
     except Exception as e:
        print(f"Error checking if employee exists: {e}")
        return False
     finally:
        cursor.close()

    def remove_employee(self, employee_id: int) -> None:
        """Remove an employee by their ID and their associated records from related tables."""

        try:
            # Check if the employee exists before attempting to remove
            if not self.employee_exists(employee_id):
                print(f"Employee ID {employee_id} does not exist in the database.")
                return
            else:
                cursor = self.connection.cursor()

             # First, delete records from related tables
                delete_tax_query = "DELETE FROM Tax WHERE EmployeeID = ?"
                delete_payroll_query = "DELETE FROM Payroll WHERE EmployeeID = ?"
                delete_financial_query = "DELETE FROM FinancialRecord WHERE EmployeeID = ?"

             # Execute delete statements for related tables
                cursor.execute(delete_tax_query, (employee_id,))
                cursor.execute(delete_payroll_query, (employee_id,))
                cursor.execute(delete_financial_query, (employee_id,))

             # Now delete the employee from the Employee table
                delete_employee_query = "DELETE FROM Employee WHERE EmployeeID = ?"
                cursor.execute(delete_employee_query, (employee_id,))

            # Commit the changes
                self.connection.commit()
                print(f"Employee ID {employee_id} and their associated records removed successfully.")

        except Exception as e:
            print(f"Failed to remove employee: {e}")
        finally:
            cursor.close()