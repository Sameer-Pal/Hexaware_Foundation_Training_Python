
#   7. Implement the IOrderManagementRepository interface/abstractclass in a class called


from dao.IOrder_management_repository import IOrderManagementRepository
from exception.custom_exceptions import UserNotFoundException, OrderNotFoundException
from util.db_connection_util import DBUtil


class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def create_order(self, user, products):
        cursor = self.connection.cursor()
        try:
            # Check if user exists
            query = "SELECT * FROM users WHERE user_id = ?"
            cursor.execute(query, (user.userId,))
            result = cursor.fetchone()

            if not result:
                # If user does not exist, create the user
                self.create_user(user)
                print(f"User {user.username} created.")

            # Insert order and associate products with the order
            query = "INSERT INTO orders (user_id) VALUES (?)"
            cursor.execute(query, (user.userId,))
            self.connection.commit()

            order_id = cursor.lastrowid  # Get the last inserted order ID

            # Insert products into order_products
            for product in products:
                query = "INSERT INTO order_products (order_id, product_id) VALUES (?, ?)"
                cursor.execute(query, (order_id, product.productId))

            self.connection.commit()
            print("Order created successfully.")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def cancel_order(self, userId, orderId):
        cursor = self.connection.cursor()
        try:
            # Check if order exists
            query = "SELECT * FROM orders WHERE order_id = ? AND user_id = ?"
            cursor.execute(query, (orderId, userId))
            result = cursor.fetchone()

            if not result:
                raise OrderNotFoundException(
                    f"Order ID {orderId} not found for User ID {userId}.")

            # Cancel order
            query = "DELETE FROM orders WHERE order_id = ? AND user_id = ?"
            cursor.execute(query, (orderId, userId))
            self.connection.commit()
            print(f"Order {orderId} canceled for User ID {userId}.")
        except OrderNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def create_product(self, user_id, product):
        cursor = self.connection.cursor()
        try:
            # Check if user exists in the database with the Admin role
            check_user_query = "SELECT * FROM users WHERE user_id = ? AND role = 'Admin'"
            cursor.execute(check_user_query, (user_id,))
            admin_user = cursor.fetchone()  # Fetch one record if it exists

            if admin_user is None:
                raise PermissionError(
                    "Admin user does not exist in the database.")

            # Insert product into the database (product_id is auto-generated)
            query = """
            INSERT INTO products (product_name, description, price, quantity_in_stock, type)
            VALUES (?, ?, ?, ?, ?)
        """
            cursor.execute(query, (product.productName, product.description,
                           product.price, product.quantityInStock, product.type))
            self.connection.commit()
            print(f"Product {product.productName} created successfully.")

        except PermissionError as e:
            print(e)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()

    def create_user(self, user):
        cursor = self.connection.cursor()
        try:
            # INSERTIN INTO DATABASE
            query = "INSERT INTO users (username, password, role) VALUES (?, ?, ?)"
            cursor.execute(query, (user.username, user.password, user.role))
            self.connection.commit()

            cursor.execute("SELECT * from Users")
            # user.userId = cursor.fetchone()[0]  # Get the ID from the result
            print(f"User {user.username} created successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def get_all_products(self):
        cursor = self.connection.cursor()
        try:
            query = "SELECT * FROM products"
            cursor.execute(query)
            products = cursor.fetchall()

            for product in products:
                print(product)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def get_order_by_user(self, user):
        cursor = self.connection.cursor()
        try:
            query = "SELECT p.product_id, p.product_name, p.description, p.price, o.order_id, u.username, u.role  FROM Orders o   JOIN Users u ON o.user_id = u.user_id    JOIN Products p ON o.product_id = p.product_id  WHERE u.user_id = ?;"
            cursor.execute(query, (user.userId,))  
            orders = cursor.fetchall()
            if not orders:
                raise UserNotFoundException(
                    f"User ID {user.userId} not found.")
            else:
                for order in orders:
                    print(order)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
