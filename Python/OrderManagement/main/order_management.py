import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

# 7. Implement the IOrderManagementRepository

from entity.product import Product
from entity.user import User
from dao.order_processor import OrderProcessor


class OrderManagement:
    def __init__(self):
        self.processor = OrderProcessor()

    def main_menu(self):
        while True:
            print(" \n  Order Management System  ")
            print("\n1. Create User")
            print("2. Create Product")
            print("3. Cancel Order")
            print("4. Get All Products")
            print("5. Get Orders by User")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_user()

            elif choice == '2':
                self.create_product()

            elif choice == '3':
                self.cancel_order()

            elif choice == '4':
                self.get_all_products()

            elif choice == '5':
                self.get_orders_by_user()

            elif choice == '6':
                break

            else:
                print("Invalid choice. Please try again.")

    def create_user(self):
     username = input("Enter username: ")
     password = input("Enter password: ")

    # For Role input[Admin/User] validation
     while True: 

        role = input("Enter role (Admin/User): ").capitalize()
        if role in ["Admin", "User"]:
            break  # Valid role, break out of the loop
        else:
            print("Invalid input! Please enter either 'Admin' or 'User'.")

     # Create the user object after validation
     user = User(username=username, password=password, role=role)
    
    # Call the processor to save the user
     self.processor.create_user(user)
     print(f"User {username} created with role {role}")

    def create_product(self):
        product = Product(
            productName=input("Enter product name: "),
            description=input("Enter description: "),
            price=float(input("Enter price: ")),
            quantityInStock=int(input("Enter quantity in stock: ")),
            type=input("Enter type (Electronics/Clothing): ").capitalize()
        )
        # Read user ID as an integer
        user_id = int(input("Enter your user ID: "))
        self.processor.create_product(user_id, product)

    def cancel_order(self):
        userId = int(input("Enter user ID: "))
        orderId = int(input("Enter order ID: "))
        self.processor.cancel_order(userId, orderId)

    def get_all_products(self):
        self.processor.get_all_products()

    def get_orders_by_user(self):
        userId = int(input("Enter user ID: "))
        user = User(userId=userId, username="", password="", role="")

        self.processor.get_order_by_user(user)


if __name__ == '__main__':
    app = OrderManagement()
    app.main_menu()
