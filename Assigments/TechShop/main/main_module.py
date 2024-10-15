import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from dao.implementationClasses.product_dao import ProductDAO
from dao.implementationClasses.order_dao import OrderDAO
from dao.implementationClasses.inventory_dao import InventoryDAO
from dao.implementationClasses.report_dao import ReportDAO
from dao.implementationClasses.payment_dao import PaymentDAO
from entity.customers import Customer
from entity.product import Product
from entity.order import Order
from dao.implementationClasses.customer_dao import CustomerDAO

class ApplicationMenu:
    def __init__(self):
        self.customer_dao = CustomerDAO()
        self.product_dao = ProductDAO()
        self.order_dao = OrderDAO()
        self.inventory_dao = InventoryDAO()
        self.report_dao = ReportDAO()
        self.payment_dao = PaymentDAO()

    def main_menu(self):
        while True:
            print("\nWELCOME TO TECH SHOP!")
            print("1. Customer Operations")
            print("2. Product Operations")
            print("3. Order Operations")
            print("4. Inventory Operations")
            print("5. Report Operations")
            print("6. Payment Operations")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.customer_operations()
            elif choice == '2':
                self.product_operations()
            elif choice == '3':
                self.order_operations()
            elif choice == '4':
                self.inventory_operations()
            elif choice == '5':
                self.report_operations()
            elif choice == '6':
                self.payment_operations()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def customer_operations(self):
        while True:
            print("\nCustomer Operations:")
            print("1. Register Customer")
            print("2. Update Customer Info")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.register_customer()
            elif choice == '2':
                self.update_customer()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def product_operations(self):
        while True:
            print("\nProduct Operations:")
            print("1. Add Product")
            print("2. Update Product")
            print("3. View All Products")
            print("4. Delete Products")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.update_product()
            elif choice == '3':
                self.view_products()
            elif choice == '4':
                self.remove_products()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def order_operations(self):
        while True:
            print("\nOrder Operations:")
            print("1. Place Order")
            print("2. View Order Status")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.place_order()
            elif choice == '2':
                self.view_order_status()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def inventory_operations(self):
        while True:
            print("\nInventory Operations:")
            print("1. Update Inventory")
            print("2. Delete Inventory Product")
            print("3. Add Product to Inventory")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.update_inventory()
            elif choice == '2':
                self.delete_inventory_products()
            elif choice == '3':
                self.add_products_inventory()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def report_operations(self):
        while True:
            print("\nReport Operations:")
            print("1. Generate Sales Report")
            print("2. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.generate_sales_report()
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")

    def payment_operations(self):
        while True:
            print("\nPayment Operations:")
            print("1. Record Payment")
            print("2. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.record_payment()
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")

    def register_customer(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        address = input("Enter address: ")
        customer = Customer(first_name, last_name, email, phone, address)
        self.customer_dao.insert_customer(customer)

    def update_customer(self):
        customer_id = input("Enter customer ID or email to update: ")
        existing_customer = self.customer_dao.get_customer_by_id_or_email(customer_id)

        if existing_customer is None:
            print("Error: Customer not found.")
            return

        print("Current Customer Details:")
        print(f"ID: {existing_customer[0]}, Name: {existing_customer[1]} {existing_customer[2]}, Email: {existing_customer[3]}, Phone: {existing_customer[4]}, Address: {existing_customer[5]}")

        first_name = input(f"Enter new first name (current: {existing_customer[1]}): ") or existing_customer[1]
        last_name = input(f"Enter new last name (current: {existing_customer[2]}): ") or existing_customer[2]
        email = input(f"Enter new email (current: {existing_customer[3]}): ") or existing_customer[3]
        phone = input(f"Enter new phone number (current: {existing_customer[4]}): ") or existing_customer[4]
        address = input(f"Enter new address (current: {existing_customer[5]}): ") or existing_customer[5]

        self.customer_dao.update_customer(customer_id, first_name, last_name, email, phone, address)

    def add_product(self):
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        product = Product(None, name, description, price)
        self.product_dao.insert_product(product)

    def place_order(self):
        products = self.product_dao.get_all_products()
        print("Fetching all products...")
        print("Product Catalog:")
        if not products:
            print("No products available.")
            return  # Exit if no products are available
        for product in products:
            print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[3]}")  # Adjust indices based on your Product structure

        customer_id = int(input("Enter customer ID: "))  # Get the customer ID
        product_id = int(input("Enter product ID: "))  # Get the product ID
        total_amount = float(input("Enter total amount: "))  # Get total amount

        self.order_dao.place_order(customer_id,product_id,total_amount, status="Confirmed")

    def update_product(self):
        product_id = int(input("Enter product ID to update: "))
        name = input("Enter new product name: ")
        description = input("Enter new product description: ")
        price = float(input("Enter new product price: "))
        category = input("Enter category")
        self.product_dao.update_product(product_id, name, description, price,category)

    def view_products(self):
        products = self.product_dao.get_all_products()
        for product in products:
            print(product)
    
    def remove_products(self):
        product_id = int(input("enter Product ID: "))
        removed_product = self.product_dao.remove_product(product_id)
        print(removed_product)

    def view_order_status(self):
        order_id = int(input("Enter order ID to check status: "))
        status = self.order_dao.get_order_status(order_id)
        if status is None:
            print("Not Present")
        else: 
            print(f"Order Status: {status}")

    def update_inventory(self):
        product_id = int(input("Enter product ID to update: "))
        quantity = int(input("Enter new quantity: "))
        self.inventory_dao.update_inventory(product_id, quantity)

    def delete_inventory_products(self):
        inventory_id = int(input("Enter inventory ID to delete: "))
        self.inventory_dao.delete_inventory_product(inventory_id)

    def add_products_inventory(self):
        product_id = int(input("Enter product ID to add to inventory: "))
        quantity = int(input("Enter quantity to add: "))  # Get quantity from user input
        self.inventory_dao.add_product(product_id, quantity)  # Ensure you pass necessary parameters as needed

    def generate_sales_report(self):
        report = self.report_dao.generate_sales_report()
        print("Sales Report:")
        for record in report:
            print(record)

    def record_payment(self):
        order_id = int(input("Enter order ID for payment: "))
        payment_method = input("Enter payment method: ")
        amount = float(input("Enter payment amount: "))
        self.payment_dao.record_payment(order_id, payment_method, amount)

    def search_and_recommendations(self):
        product_name = input("Enter product name to search (or leave blank): ")
        category = input("Enter product category to search (mandatory) : ")
        min_price = input("Enter minimum price to search (or leave blank): ")
        max_price = input("Enter maximum price to search (or leave blank): ")

        recommendations = self.product_dao.search_and_recommendations(product_name, category, min_price, max_price)
        print("Recommended Products:")
        for product in recommendations:
            print(product)

if __name__ == "__main__":
    app = ApplicationMenu()
    app.main_menu()
