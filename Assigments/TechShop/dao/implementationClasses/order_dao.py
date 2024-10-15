
from util.db_conn_util import DBUtil
from entity.order import Order
from dao.implementationClasses.product_dao import ProductDAO
import datetime
from   dao.abtractClasses.order_dao import * 


class OrderDAO:
    def __init__(self):
        self.connection = DBUtil.getDBConn()
        self.product_dao = ProductDAO()
  
    def place_order(self, customer_id, product_id, total_amount, status="Confirmed"):
        cursor = self.connection.cursor()
        try:
            # Check if the customer exists
            cursor.execute("SELECT * FROM CUSTOMERS WHERE CustomerID = ?", (customer_id,))
            if cursor.fetchone() is None:
                print(f"Error: Customer ID {customer_id} not found.")
                return

            # Fetch the product price
            cursor.execute("SELECT Price FROM Products WHERE ProductID = ?", (product_id,))
            product = cursor.fetchone()

            if product is None:
                print(f"Error: Product ID {product_id} not found.")
                self.connection.rollback()
                return

            product_price = product[0]  # Assuming price is the first column

            # Insert order into the Orders table
            cursor.execute(
                "INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, OrderStatus) VALUES (?, ?, ?, ?)",
                (customer_id, datetime.datetime.now(), total_amount, status)
            )

            # Get the newly inserted OrderID
            order_id = cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()[0]

            # Check Inventory
            cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?", (product_id,))
            inventory_item = cursor.fetchone()

            if inventory_item is None:
                print(f"Error: Product with Product ID {product_id} is not available in inventory.")
                self.connection.rollback()
                return
            elif inventory_item[0] > 0:
                # Decrement inventory by 1
                cursor.execute(
                    "UPDATE Inventory SET QuantityInStock = QuantityInStock - 1 WHERE ProductID = ?",
                    (product_id,)
                )
                print(f"Decremented quantity for Product ID {product_id} in inventory.")
            else:
                print(f"Insufficient stock for Product ID {product_id}. Order cannot be placed.")
                self.connection.rollback()
                return

            # Calculate subtotal for this order
            subtotal = product_price * 1  # Assuming quantity is 1 for this order

            # Insert the order details into the OrderDetails table
            cursor.execute(
                "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (?, ?, ?)",
                (order_id, product_id, 1)  # Assuming quantity is 1
            )

            # Update the TotalAmount in the Orders table
            cursor.execute("UPDATE Orders SET TotalAmount = ? WHERE OrderID = ?", (subtotal, order_id))
            self.connection.commit()

            print(f"Order placed successfully. Total amount: {subtotal:.2f}")
        except Exception as e:
            print(f"Error placing order: {e}")
            self.connection.rollback()
        finally:
            cursor.close()      
    def get_order_status(self, order_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT OrderStatus FROM Orders WHERE OrderId=?", (order_id))
            order_status = cursor.fetchone()
            return order_status if order_status else None
        except Exception as e:
            print(f"Error retrieving order status: {e}")
        finally:
            cursor.close()

    def update_order_status(self, order_id, new_status):
        cursor = self.connection.cursor()
        try:
            # Check if the order exists
            cursor.execute("SELECT * FROM Orders WHERE OrderID = ?", (order_id,))
            if cursor.fetchone() is None:
                print(f"Error: Order ID {order_id} not found.")
                return

            # Update the order status
            cursor.execute("UPDATE Orders SET OrderStatus = ? WHERE OrderID = ?", (new_status, order_id))
            self.connection.commit()
            print(f"Order ID {order_id} status updated to '{new_status}'.")

            # Additional logic can be added here to synchronize with inventory if needed
        except Exception as e:
            print(f"Error updating order status: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def remove_canceled_orders(self):
        cursor = self.connection.cursor()
        try:
            # Fetch all canceled orders
            cursor.execute("SELECT OrderID FROM Orders WHERE OrderStatus = 'Canceled'")
            canceled_orders = cursor.fetchall()

            if not canceled_orders:
                print("No canceled orders found.")
                return

            for order in canceled_orders:
                order_id = order[0]

                # Restore the inventory by increasing the stock for the canceled order
                cursor.execute("SELECT ProductID FROM OrderDetails WHERE OrderID = ?", (order_id,))
                order_details = cursor.fetchall()

                for detail in order_details:
                    product_id = detail[0]
                    cursor.execute("UPDATE Inventory SET QuantityInStock = QuantityInStock + 1 WHERE ProductID = ?", (product_id,))

                # Remove the order details
                cursor.execute("DELETE FROM OrderDetails WHERE OrderID = ?", (order_id,))
                
                # Remove the order itself
                cursor.execute("DELETE FROM Orders WHERE OrderID = ?", (order_id,))
                print(f"Canceled order ID {order_id} has been removed successfully.")

            self.connection.commit()

        except Exception as e:
            print(f"Error removing canceled orders: {e}")
            self.connection.rollback()
        finally:
            cursor.close()
    def retrieve_orders(self):
         """Retrieve all orders from the database."""
         cursor = self.connection.cursor()
         try:
            cursor.execute("SELECT * FROM Orders")
            orders = cursor.fetchall()
            return [Order(*order) for order in orders]  # Adjust based on your Order class constructor
         except Exception as e:
            print(f"Error retrieving orders: {e}")
            return []
         finally:
            cursor.close()

    def sort_orders_by_date(self, ascending=True):
        """Sort orders by order date.

        Args:
            ascending (bool): If True, sort in ascending order, otherwise descending.
        """
        orders = self.retrieve_orders()
        orders.sort(key=lambda x: x._order_date, reverse=not ascending)  # Assuming _order_date is a datetime object
        return orders


    def get_orders_by_date_range(self, start_date, end_date):
        """Retrieve orders within a specific date range.

        Args:
            start_date (datetime): Start of the date range.
            end_date (datetime): End of the date range.
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM Orders WHERE OrderDate BETWEEN ? AND ?",
                (start_date, end_date)
            )
            orders = cursor.fetchall()
            return [Order(*order) for order in orders]  # Assuming Order constructor matches the fetched columns
        except Exception as e:
            print(f"Error retrieving orders by date range: {e}")
            return []
        finally:
            cursor.close()