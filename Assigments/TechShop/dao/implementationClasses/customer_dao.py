from util.db_conn_util import DBUtil
from entity.customers import Customer
import re  

class CustomerDAO:
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def is_valid_email(self, email: str) -> bool:
        """Validates email format using regex."""
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(email_regex, email) is not None


    def insert_customer(self, customer):
        cursor = self.connection.cursor()
        try:
        # Check if the first name contains only alphabetic characters
            if not customer.first_name.isalpha():
                print("Error: First name should contain only letters.")
                return
        # Check if the first name contains only alphabetic characters
            if not customer.last_name.isalpha():
                print("Error: Last name should contain only letters.")
                return

            if not self.is_valid_email(customer.email):
                print("Error: Invalid email format.")
                return

            # Check for duplicate email
            cursor.execute("SELECT * FROM Customers WHERE Email = ?", (customer.email,))
            if cursor.fetchone():
                print("Email already exists.")
                return


            # Insert customer into the database
            cursor.execute("SELECT * FROM Customers WHERE Email = ?", (customer.email,))
            if cursor.fetchone():
                print("Error: Email already exists.")
                return

            cursor.execute("INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?)",
                           (customer.first_name,customer.last_name, customer.email, customer.phone,customer.address))
            self.connection.commit()
            print(f"Customer  registered successfully.")
        except Exception as e:
            print(f"Error inserting customer: {e}")
        finally:
            cursor.close()

    def get_all_customers(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Customers")
        customers = cursor.fetchall()
        cursor.close()
        return customers


    def update_customer(self, customer_id, first_name, last_name, email, phone, address):
     cursor = self.connection.cursor()
     try:
        if not self.is_valid_email(email):
            print("Error: Invalid email format.")
            return

        cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
        if cursor.fetchone() is None:
            print("Error: Customer not found.")
            return

            # Check if customer exists by ID
        cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
        if cursor.fetchone() is None:
                print("Customer not found.")
                return

        cursor.execute(
            """
            UPDATE Customers 
            SET FirstName = ?, LastName = ?, Email = ?, Phone = ?, Address = ? 
            WHERE CustomerID = ?
            """,
            (first_name, last_name, email, phone, address, customer_id)
        )
        self.connection.commit()
        print("Customer updated successfully.")
     except Exception as e:
        print(f"Error updating customer: {e}")
     finally:
        cursor.close()

    def get_customer_by_id_or_email(self, identifier):
        cursor = self.connection.cursor()
        try:
            # Check if the identifier is numeric (indicating a Customer ID)
            if identifier.isdigit():
                # Fetch customer by CustomerID
                cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (identifier,))
            else:
                # Otherwise, fetch by email
                cursor.execute("SELECT * FROM Customers WHERE Email = ?", (identifier,))
            
            customer = cursor.fetchone()  # Fetch one result
            return customer  # Return customer data (tuple) or None if not found
        except Exception as e:
            print(f"Error fetching customer: {e}")
            return None
        finally:
             cursor.close()  # Ensure the cursor is closed to free resources
