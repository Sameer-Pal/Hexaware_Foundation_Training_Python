from util.db_conn_util import DBUtil
from entity.product import Product
from   dao.abtractClasses.product_dao import * 

class ProductDAO:
    def __init__(self):
        self.connection = DBUtil.getDBConn()

    def insert_product(self, product):
        cursor = self.connection.cursor()
        try:

              cursor.execute("SELECT COUNT(*) FROM Products WHERE ProductName = ? AND ProductID != ?", 
                       (product.product_name, product.product_id))
              name_exists = cursor.fetchone()[0] > 0
    
              if name_exists:
                    print(f"A product with the name '{product.product_name}' already exists. Update failed.")
                    return  # Exit the method without making changes

              cursor.execute("INSERT INTO Products  (ProductName, Description, Price) VALUES (?, ?, ?)",
                           (product._product_name, product._description, product._price))
              self.connection.commit()
              print("Product added successfully.")
        except Exception as e:
            print(f"Error inserting product: {e}")
        finally:
            cursor.close()

# product_dao.py

    def update_product(self, product_id, name, description, price,category):
     cursor = self.connection.cursor()
     try:
        cursor.execute("""
            UPDATE Products 
            SET ProductName=?, description=?, price=?,Categories=?
            WHERE ProductID=?
        """, (name, description, price,category, product_id))
        self.connection.commit()
        print("Product updated successfully.")
     except Exception as e:
        print(f"Error updating product: {e}")
     finally:
        cursor.close()

    def get_all_products(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
        cursor.close()
        return products
    
    def search_and_recommendations(self, product_name, category):
     cursor = self.connection.cursor()
    
    # Build the SQL query based on optional product name and mandatory category
     query = "SELECT * FROM Products WHERE Categories = ?"
     params = [category]  # Start with the mandatory category filter

    # If product name is provided, add it to the query
     if product_name:
        query += " OR ProductName LIKE ?"
        params.append(f"%{product_name}%")  # Use LIKE for partial matches

    # Execute the search query
     cursor.execute(query, params)
     search_results = cursor.fetchall()

    # Display search results
     if search_results:
        print("\nSearch Results:")
        for product in search_results:
            # Use the actual column names returned from the query
            print(f" Name: {product.ProductName}, Category: {product.Categories}, Price: {product.Price}")

        # Recommendations based on the category
        cursor.execute("SELECT * FROM Products WHERE Categories = ?", (category))
        recommendations = cursor.fetchall()

        # Display recommendations
        if recommendations:
            print("\nRecommendations :")
            for product in recommendations:
                # Use the actual column names returned from the query
                print(f" Name: {product.ProductName}, Category: {product.Categories}, Price: {product.Price}")
        else:
            print("No recommendations found for this category.")
     else:
        print("No products found.")

     cursor.close()



    def remove_product(self, product_id):
        cursor = self.connection.cursor()
        try:
            # Check if the product exists
            cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
            product = cursor.fetchone()

            if not product:
                print(f"Product with ID {product_id} not found.")
                return

            # First, delete all related records in the Inventory table
            cursor.execute("DELETE FROM Inventory WHERE ProductID = ?", (product_id,))
            self.connection.commit()
            print(f"Related records in Inventory for Product ID {product_id} removed successfully.")

            # Now delete the product from the Products table
            cursor.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
            self.connection.commit()
            print(f"Product with ID {product_id} removed successfully from Products.")

        except Exception as e:
            print(f"Error removing product: {e}")
        finally:
            cursor.close()