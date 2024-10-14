import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn() -> pyodbc.Connection:
        """Establish a connection to the database and return the connection object."""
        connection_string = (
            r'Driver={SQL Server};'
            r'Server=DESKTOP-804A2VF\SQLEXPRESS10;'  # Change as per your setup
            'Database=PayXpert;'
            'Trusted_Connection=yes;'
        )
        try:
            connection = pyodbc.connect(connection_string)
            print("Connected Successfully")
            return connection
        except Exception as e:
            print(f"Connection failed: {e}")
            return None
