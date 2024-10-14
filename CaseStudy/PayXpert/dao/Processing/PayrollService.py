from typing import List, Dict, Any
from util.db_conn_util import DBUtil
from dao.Abstract_Classes.IPayrollService import PayrollService

class PayrollServiceImpl(PayrollService):
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def calculate_basic_salary(self, employee_id):
        cursor = self.connection.cursor()
        try:
            query = "SELECT BasicSalary FROM Payroll WHERE EmployeeID = ?"
            cursor.execute(query, (employee_id,))
            basic_salary = cursor.fetchone()

            if basic_salary:
                return basic_salary[0]
            else:
                raise Exception(f"No basic salary found for employee ID {employee_id}")
        finally:
            cursor.close()

    def calculate_overtime_pay(self, employee_id):
        cursor = self.connection.cursor()
        try:
            query = "SELECT OvertimePay FROM Payroll WHERE EmployeeID = ?"
            cursor.execute(query, (employee_id,))
            overtime_pay = cursor.fetchone()

            if overtime_pay:
                return overtime_pay[0]
            else:
                return 0
        finally:
            cursor.close()

    def calculate_deductions(self, employee_id):
        cursor = self.connection.cursor()
        try:
            query = "SELECT Deductions FROM Payroll WHERE EmployeeID = ?"
            cursor.execute(query, (employee_id,))
            deductions = cursor.fetchone()

            if deductions:
                return deductions[0]
            else:
                return 0
        finally:
            cursor.close()

    def generate_payroll(self, employee_id, start_date, end_date):
        cursor = self.connection.cursor()
        try:

         cursor.execute("SELECT COUNT(*) FROM Employee WHERE EmployeeID = ?", (employee_id,))
         exists = cursor.fetchone()[0] > 0

         if not exists:
            print(f"Employee ID {employee_id} does not exist in the database.")
            return  # Exit the function if the employee does not exist
        
         basic_salary = self.calculate_basic_salary(employee_id)
         overtime_pay = self.calculate_overtime_pay(employee_id)
         deductions = self.calculate_deductions(employee_id)

         net_salary = basic_salary + overtime_pay - deductions

         query = """
                 INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
         cursor.execute(query, (employee_id, start_date, end_date, basic_salary, overtime_pay, deductions, net_salary))  
         self.connection.commit()
         print(f"Payroll generated successfully for employee ID {employee_id}")
         print(f"Payroll generated successfully for Employee ID {employee_id}")
         print("Payroll Details:")
         print(f"  Pay Period: {start_date} to {end_date}")
         print(f"  Basic Salary: {basic_salary:.2f}")
         print(f"  Overtime Pay: {overtime_pay:.2f}")
         print(f"  Deductions: {deductions:.2f}")
         print(f"  Total Amount to be Paid: {net_salary:.2f}")
         return True
        except Exception as e:
            print(f"Error generating payroll: {e}")
        finally:
            cursor.close()    


    def get_payroll_by_payrolId(self, payroll_id: int) -> Dict[str, Any]:
        """Get payroll details by payroll ID."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Payroll WHERE PayrollID = ?"
            cursor.execute(query, (payroll_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "payroll_id": row.PayrollID,
                    "employee_id": row.EmployeeID,
                    "pay_period_start_date": row.PayPeriodStartDate,
                    "pay_period_end_date": row.PayPeriodEndDate,
                    "basic_salary": row.BasicSalary,
                    "overtime_pay": row.OvertimePay,
                    "deductions": row.Deductions,
                    "net_salary": row.NetSalary
                }
            else:
                raise ValueError(f"Payroll with ID {payroll_id} not found.")
        except Exception as e:
            print(f"Failed to fetch payroll: {e}")
            return {}
        finally:
            cursor.close()

    def get_payrolls_for_employeeID(self, employee_id: int) -> List[Dict[str, Any]]:
        """Get all payroll records for a specific employee."""
        payrolls = []
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Payroll WHERE EmployeeID = ?"
            cursor.execute(query, (employee_id,))
            rows = cursor.fetchall()
            for row in rows:
                payrolls.append({
                    "payroll_id": row.PayrollID,
                    "employee_id": row.EmployeeID,
                    "pay_period_start_date": row.PayPeriodStartDate,
                    "pay_period_end_date": row.PayPeriodEndDate,
                    "basic_salary": row.BasicSalary,
                    "overtime_pay": row.OvertimePay,
                    "deductions": row.Deductions,
                    "net_salary": row.NetSalary
                })
            return payrolls
        except Exception as e:
            print(f"Failed to fetch payrolls for employee: {e}")
            return []
        finally:
            cursor.close()

    def get_payrolls_for_period(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """Get all payroll records for a specific period."""
        payrolls = []
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT * FROM Payroll
                WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?
            """
            cursor.execute(query, (start_date, end_date))
            rows = cursor.fetchall()
            for row in rows:
                payrolls.append({
                    "payroll_id": row.PayrollID,
                    "employee_id": row.EmployeeID,
                    "pay_period_start_date": row.PayPeriodStartDate,
                    "pay_period_end_date": row.PayPeriodEndDate,
                    "basic_salary": row.BasicSalary,
                    "overtime_pay": row.OvertimePay,
                    "deductions": row.Deductions,
                    "net_salary": row.NetSalary
                })
            return payrolls
        except Exception as e:
            print(f"Failed to fetch payrolls for period: {e}")
            return []
        finally:
            cursor.close()

