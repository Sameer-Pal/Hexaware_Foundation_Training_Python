from util.db_conn_util import DBUtil
from entity.inventory import Inventory
from datetime import datetime
from   dao.abtractClasses.inventory_dao import * 

class InventoryDAO:
    def __init__(self):
        self.connection = DBUtil.getDBConn()



    # def add_product(self, product_id, quantity):  # Accept quantity as a parameter
    def add_product(self, product_id, quantity):  # Accept quantity as a parameter
        cursor = self.connection.cursor()
        try:
            # Check if the product exists in the Products table
            cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
            product_exists = cursor.fetchone()

            if product_exists is None:
                print(f"Product ID {product_id} does not exist in Products table.")
                return  # Exit the method if the product does not exist

            # Check if the product already exists in the Inventory table
            cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?", (product_id,))
            inventory_item = cursor.fetchone()

            if inventory_item is None:
                # Product does not exist in inventory, so add it
                cursor.execute("INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate) VALUES (?, ?, ?)",
                               (product_id, quantity, datetime.now()))
                self.connection.commit()
                print("Product added to inventory.")
            else:
                print(f"Product ID {product_id} already exists in inventory. Updating quantity...")
                # Update the existing quantity
                new_quantity = inventory_item[0] + quantity  # Add new quantity to existing quantity
                cursor.execute("UPDATE Inventory SET QuantityInStock = ?, LastStockUpdate = ? WHERE ProductID = ?",
                               (new_quantity, datetime.now(), product_id))
                self.connection.commit()
                print("Product quantity updated in inventory.")

        except Exception as e:
            print(f"Error adding product to inventory: {e}")
            self.connection.rollback()  # Rollback in case of error
        finally:
            cursor.close()


    def update_inventory(self, product_id, quantity):
        cursor = self.connection.cursor()
        try:
            # Check if product exists in Inventory table
            cursor.execute("UPDATE Inventory SET QuantityInStock = ?, LastStockUpdate = ? WHERE ProductID = ?",
                           (quantity, datetime.now(), product_id))
            if cursor.rowcount == 0:
                print(f"No product found with ID {product_id} to update.")
            else:
                self.connection.commit()
                print("Inventory updated successfully.")

        except Exception as e:
            print(f"Error updating inventory: {e}")
            self.connection.rollback()  # Rollback in case of error
        finally:
            cursor.close()

    def delete_inventory_product(self, inventory_id):
        cursor = self.connection.cursor()
        try:
            # Check if product exists in Inventory table
            cursor.execute("DELETE FROM Inventory WHERE InventoryID = ?", (inventory_id,))
            if cursor.rowcount == 0:
                print(f"No product found with Inventory ID {inventory_id} to delete.")
            else:
                self.connection.commit()
                # cursor.execute("DELETE FROM Products WHERE InventoryID = ?", (inventory_id,))

                print("Product removed from inventory.")

        except Exception as e:
            print(f"Error removing product from inventory: {e}")
            self.connection.rollback()  # Rollback in case of error
        finally:
            cursor.close()
            
    def get_all_inventory(self):
        """Retrieve all inventory items sorted by product ID."""
        sorted_inventory = sorted(self.inventory.values(), key=lambda inv: inv.product_id)
        return sorted_inventory
