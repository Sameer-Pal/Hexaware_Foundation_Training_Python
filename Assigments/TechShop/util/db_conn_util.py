import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn() -> pyodbc.Connection:
        """Establish a connection to the database and return the connection object."""
        connection_string = (
            r'Driver={SQL Server};'
            r'Server=DESKTOP-804A2VF\SQLEXPRESS10;'
            'Database=Tech_Shop;'   
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
if db_connection:
        # Use the connection for operations
        cursor = db_connection.cursor()
        
#         # Example of using the cursor (you can execute SQL queries here)
# cursor.execute("SELECT * FROM Products where Categories= 'electronics'")
# rows = cursor.fetchall()
# for row in rows:
#             print(row)

# cursor.execute("SELECT * FROM Products where categories=electronics")
# rows = cursor.fetchall()
# for row in rows:
#             print(row)
        # Don't forget to close the connection when done
db_connection.close()
