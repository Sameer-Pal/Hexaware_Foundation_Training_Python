
from datetime import datetime


from entity.customers import Customer  # Use a relative import

from exception.Insufficient_Stock_Excpetion import InsufficientStockException
from exception.Payment_Exception import PaymentFailedException
from exception.Concurrency_Exception import ConcurrencyException
class Order:
    def __init__(self, customer,product_id ,total_amount,status,order_date=None,last_updated=None,order_id=None):
        self._order_id = order_id
        # Composition: Order has a Customer object
        self._customer = customer     # custoemrID
        self._product_id =product_id
        self._order_date = order_date or datetime.now()
        self.status = status
        self._total_amount = total_amount  # Default total amount
        self._order_details = []  # To store details related to the order
        # return self._last_updated
        self._last_updated = last_updated or datetime.now()



    # Getter and setter for order_id
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        if isinstance(value, int) and value > 0:
            self._order_id = value
        else:
            raise ValueError("Order ID must be a positive integer.")

    # Getter and setter for customer
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Invalid customer. must be a Customer Object")
        

    # Getter and setter for order_date
    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, value):
        if isinstance(value, datetime):
            self._order_date = value
        else:
            raise ValueError("Order date must be a datetime object.")


    # Getter and setter for total_amount
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._total_amount = value
        else:
            raise ValueError("Total amount must be a non-negative number.")

    def calculate_total_amount(self):
        self.total_amount = sum([od.calculate_subtotal() for od in self.order_details])
        return self.total_amount

    def get_order_details(self):
        details = f"Order ID: {self.order_id}, Customer: {self.customer.get_customer_details()}, Order Date: {self.order_date}, Total Amount: {self.total_amount}\n"
        details += "\n".join([od.get_order_detail_info() for od in self.order_details])
        return details

    def update_order_status(self, status):
        self.status = status
        print(f"Order status updated to {status}")

    def cancel_order(self):
        self.order_details = []
        self.total_amount = 0
        print("Order has been canceled and stock levels adjusted.")


    def process_order(self):
        try:
            for order_detail in self.order_details:
                # Check if enough stock is available for each product
                inventory = order_detail.product.inventory
                inventory.remove_from_inventory(order_detail.quantity)
            
            # If all products are in stock, finalize the order
            self.order_status = "Processing"
            print(f"Order {self.order_id} is being processed.")
        
        except InsufficientStockException as e:
            self.order_status = "Failed"
            print(f"Order {self.order_id} failed: {e}")

    def process_payment(self, payment_method, amount):
        try:
            # Simulate payment processing (this could be an API call in real-world applications)
            if not self.simulate_payment(payment_method, amount):
                raise PaymentFailedException(f"Payment for Order {self.order_id} was declined.")
            
            # Payment successful
            self.order_status = "Paid"
            print(f"Payment for Order {self.order_id} was successful.")
        
        except PaymentFailedException as e:
            self.order_status = "Payment Failed"
            print(f"Order {self.order_id} failed due to payment issue: {e}")
            # Optionally, trigger retry or cancellation logic here
            self.retry_or_cancel_payment()
    def retry_payment(self):
        # Here we simulate retrying the payment (you could re-call process_payment)
        print(f"Retrying payment for Order {self.order_id}...")
        self.process_payment("CreditCard", self.total_amount)

    def cancel_order(self):
        # Mark the order as cancelled
        self.order_status = "Cancelled"
        print(f"Order {self.order_id} has been cancelled.")

    # Getters and Setters for attributes
    @property
    def last_updated(self):
        return self._last_updated
    
    def update_order(self, new_status, db_last_updated):
        """
        Update the order status if the last updated timestamp matches.
        :param new_status: The new status of the order.
        :param db_last_updated: The last_updated value stored in the database.
        """
        # Check if the current object's last_updated timestamp matches the DB value
        if db_last_updated != self._last_updated:
            raise ConcurrencyException("This order has been updated by another user. Please refresh the data and try again.")