
import pyodbc
from util.db_conn_util import DBUtil  # Assuming the DBUtil class is in this path


class DatabaseContext:
    def __init__(self):
        self.connection = DBUtil.getDBConn()  # Get the DB connection using DBUtil

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def execute_query(self, query, params=None):
        """Execute a single query."""
        with self.connection.cursor() as cursor:
            cursor.execute(query, params or ())
            self.connection.commit()

    def fetch_query(self, query, params=None):
        """Fetch results from a query."""
        with self.connection.cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()

# Example usage
if __name__ == "__main__":
    db_context = DatabaseContext()
    db_context.close()
