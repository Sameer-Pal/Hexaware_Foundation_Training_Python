import pyodbc
# 8. Create DBUtil class


class DBUtil:
    @staticmethod
    def getDBConn() -> pyodbc.Connection:
        """Establish a connection to the database and return the connection object."""
        connection_string = (
            r'Driver={SQL Server};'
            r'Server=DESKTOP-804A2VF\SQLEXPRESS09;'
            'Database=OrderManagement;'
            'Trusted_Connection=yes;'
        )
        try:
            connection = pyodbc.connect(connection_string)
            print("Connected Successfully")
            return connection
        except Exception as e:
            print("Connection failed: {}".format(e))
            return None


db_connection = DBUtil.getDBConn()
