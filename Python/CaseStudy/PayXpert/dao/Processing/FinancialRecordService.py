from typing import List, Dict, Any
from dao.Abstract_Classes.IFinancialRecordService import FinancialRecordService
from util.db_conn_util import DBUtil

class FinancialRecordServiceImpl(FinancialRecordService):
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def add_financial_record(self, employee_id, description, amount, record_type):
        """Add a financial record for an employee."""
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,))
            exists = cursor.fetchone()[0] >0
            if not exists:
                print(f"Employee ID {employee_id} does not exist in the database.")
                return  # Exit the function if the employee does not exist

            query = """
                INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType) 
                VALUES (?, GETDATE(), ?, ?, ?)
            """
            cursor.execute(query, (employee_id, description, amount, record_type))
            self.connection.commit()
            print("Financial record added successfully.")
        except Exception as e:
            print(f"Error adding financial record: {e}")


    def get_financial_record_by_id(self, record_id: int) -> Dict[str, Any]:
        """Get financial record details by record ID."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM FinancialRecord WHERE RecordID = ?"
            cursor.execute(query, (record_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "record_id": row.RecordID,
                    "employee_id": row.EmployeeID,
                    "record_date": row.RecordDate,
                    "description": row.Description,
                    "amount": row.Amount,
                    "record_type": row.RecordType
                }
            else:
                raise ValueError(f"Financial record with ID {record_id} not found.")
        except Exception as e:
            print(f"Failed to fetch financial record: {e}")
            return {}
        finally:
            cursor.close()

    def get_financial_records_for_employee(self, employee_id: int) -> List[Dict[str, Any]]:
        """Get all financial records for a specific employee."""
        records_for_employee = []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM FinancialRecord WHERE EmployeeID = ?"
            cursor.execute(query, (employee_id,))
            rows = cursor.fetchall()
            for row in rows:
                records_for_employee.append({
                    "record_id": row.RecordID,
                    "employee_id": row.EmployeeID,
                    "record_date": row.RecordDate,
                    "description": row.Description,
                    "amount": row.Amount,
                    "record_type": row.RecordType
                })
            if  len(records_for_employee)==0:
                print(f"No financial records found for Employee {employee_id}.")
            else:
                return records_for_employee
        except Exception as e:
            print(f"Failed to fetch financial records for employee {employee_id}: {e}")
        finally:
            cursor.close()
        return records_for_employee

    def get_financial_records_for_date(self, record_date: str) -> List[Dict[str, Any]]:
        """Get all financial records for a specific date."""
        records_for_date = []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM FinancialRecord WHERE RecordDate = ?"
            cursor.execute(query, (record_date,))
            rows = cursor.fetchall()
            for row in rows:
                records_for_date.append({
                    "record_id": row.RecordID,
                    "employee_id": row.EmployeeID,
                    "record_date": row.RecordDate,
                    "description": row.Description,
                    "amount": row.Amount,
                    "record_type": row.RecordType
                })
            if len(records_for_date)==0:
                print(f"No financial records found for Date {record_date}.")
            else:
                return records_for_date
        except Exception as e:
            print(f"Failed to fetch financial records for date {record_date}: {e}")
        finally:
            cursor.close()
        return records_for_date

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
