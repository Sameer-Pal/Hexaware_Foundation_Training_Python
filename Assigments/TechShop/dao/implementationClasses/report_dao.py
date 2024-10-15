from util.db_conn_util import DBUtil

class ReportDAO:
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def generate_sales_report(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM Orders o Join OrderDetails od ON od.OrderID = o.OrderID")  # Adjust the query to fit your needs
            sales_data = cursor.fetchall()

            # Define column names for clarity
            column_names = ['OrderID', 'ProductID', 'Quantity', 'OrderDate', 'TotalAmount']

            # Create a list of dictionaries for better structure
            report = []
            for row in sales_data:
                report.append(dict(zip(column_names, row)))

            return report
        except Exception as e:
            print(f"Error generating sales report: {e}")
            return None  # Return None or an empty list in case of an error
        finally:
            cursor.close