from util.db_conn_util import DBUtil
from decimal import Decimal
from   dao.abtractClasses.payment_dao import * 

class PaymentDAO:
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def record_payment(self, order_id: int, payment_method: str, amount: Decimal) -> bool:
        cursor = None
        try:
            cursor = self.connection.cursor()

            # Step 1: Validate the payment amount
            if amount <= Decimal('0.00'):
                raise ValueError("Payment amount must be greater than zero.")

            # Step 2: Check if the order exists
            check_order_query = "SELECT COUNT(*) FROM Orders WHERE OrderId = ?"
            cursor.execute(check_order_query, (order_id,))
            order_exists = cursor.fetchone()[0]

            if order_exists == 0:
                print(f"Order ID {order_id} does not exist.")
                return False

            # Step 3: Update the Orders table with payment method and amount
            update_order_query = """
                UPDATE Orders 
                SET PaymentMethod = ?, TotalAmount = ? 
                WHERE OrderId = ?;
            """
            cursor.execute(update_order_query, (payment_method, amount, order_id))

            # Step 4: Commit the transaction
            self.connection.commit()

            print("Payment recorded successfully.")
            return True


        except ValueError as value_error:
            print(f"Validation error: {value_error}")
            return False

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
