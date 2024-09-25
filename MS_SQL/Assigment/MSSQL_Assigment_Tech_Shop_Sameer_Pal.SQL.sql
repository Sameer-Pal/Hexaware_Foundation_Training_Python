

Create Database Tech_Shop;
/*1. Customers:
• CustomerID (Primary Key)
• FirstName
• LastName
• Email
• Phone
• Address*/
CREATE TABLE CUSTOMERS(
CustomerID int Identity Primary Key,
FirstName varchar(30),
LastName varchar(30),
Email varchar(30),
Phone varchar(30),
Address varchar(40)
);
/*. Products:
• ProductID (Primary Key)
• ProductName
• Description
• Price
*/
create table Products(
ProductID int Identity Primary Key,
ProductName varchar(30),
Description varchar(80),
Price int
);
/*
Orders:
• OrderID (Primary Key)
• CustomerID (Foreign Key referencing Customers)
• OrderDate
• TotalAmount*/
create table Orders(
OrderID int Identity Primary Key,
CustomerID int Foreign key references Customers(CustomerID),
OrderDate date,
TotalAmount int
);
/*OrderDetails:
• OrderDetailID (Primary Key)
• OrderID (Foreign Key referencing Orders)
• ProductID (Foreign Key referencing Products)
• Quantity*/
create table OrderDetails(
OrderDetail int Identity Primary key,
OrderID int foreign key references Orders(OrderID),
ProductID int foreign key references Products(ProductID),
Quantity int
);
/*Inventory
• InventoryID (Primary Key)
• ProductID (Foreign Key referencing Products)
• QuantityInStock
• LastStockUpdate*/
create table Inventory(
InventoryID int Identity Primary key,
ProductID int foreign key references Products(ProductID),
QuantityInStock int,
LastStockUpdate date
);
select * from Products

select * from OrderDetails
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES
('John', 'Doe', 'john.doe@example.com', '555-1234', '123 Elm St'),
('Jane', 'Smith', 'jane.smith@example.com', '555-5678', '456 Oak St'),
('Alice', 'Johnson', 'alice.j@example.com', '555-8765', '789 Pine St'),
('Bob', 'Brown', 'bob.brown@example.com', '555-4321', '101 Maple St'),
('Charlie', 'Davis', 'charlie.davis@example.com', '555-9876', '102 Cedar St'),
('David', 'Wilson', 'david.wilson@example.com', '555-1122', '222 Birch St'),
('Eva', 'Taylor', 'eva.taylor@example.com', '555-3344', '333 Walnut St'),
('Frank', 'Thomas', 'frank.thomas@example.com', '555-5566', '444 Chestnut St'),
('Grace', 'Moore', 'grace.moore@example.com', '555-7788', '555 Spruce St'),
('Harry', 'Anderson', 'harry.anderson@example.com', '555-9911', '666 Aspen St'),
('Ivy', 'Clark', 'ivy.clark@example.com', '555-2233', '777 Willow St'),
('Jack', 'Martin', 'jack.martin@example.com', '555-4455', '888 Redwood St'),
('Kelly', 'Lee', 'kelly.lee@example.com', '555-6677', '999 Cedar St'),
('Liam', 'Harris', 'liam.harris@example.com', '555-8899', '123 Maplewood St'),
('Mia', 'Walker', 'mia.walker@example.com', '555-1212', '456 Oakwood St'),
('Noah', 'Young', 'noah.young@example.com', '555-3434', '789 Pinewood St'),
('Olivia', 'King', 'olivia.king@example.com', '555-5656', '101 Birchwood St'),
('Paul', 'Scott', 'paul.scott@example.com', '555-7878', '202 Elmwood St'),
('Quinn', 'Adams', 'quinn.adams@example.com', '555-9090', '303 Cedarwood St'),
('Rachel', 'Baker', 'rachel.baker@example.com', '555-0101', '404 Maple St');
INSERT INTO Products (ProductName, Description, Price) VALUES
('Laptop', '15-inch display, 8GB RAM', 799.99),
('Smartphone', '5G enabled, 64GB storage', 599.99),
('Tablet', '10-inch screen, 32GB storage', 299.99),
('Headphones', 'Noise-canceling, over-ear', 199.99),
('Smartwatch', 'Fitness tracker, heart-rate monitor', 149.99),
('Gaming Console', 'Next-gen gaming console', 499.99),
('Wireless Mouse', 'Bluetooth mouse, ergonomic design', 29.99),
('Mechanical Keyboard', 'RGB backlit, Cherry MX switches', 99.99),
('Monitor', '27-inch 4K display', 399.99),
('External SSD', '1TB, USB-C, Portable', 149.99),
('Portable Charger', '10,000mAh, fast charging', 49.99),
('Smart Speaker', 'Voice-controlled, built-in assistant', 129.99),
('Bluetooth Earbuds', 'Wireless, noise-canceling', 89.99),
('VR Headset', 'Virtual reality, high resolution', 599.99),
('Smart Home Hub', 'Control smart devices, voice assistant', 99.99),
('Drone', '4K camera, GPS navigation', 799.99),
('Fitness Band', 'Activity tracker, heart-rate monitor', 59.99),
('Camera', 'DSLR, 24MP, 18-55mm lens', 899.99),
('Smart Thermostat', 'WiFi-enabled, energy saving', 199.99),
('E-reader', '6-inch display, 8GB storage', 129.99);
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES
(1, '2023-01-15', 1099.98),
(2, '2023-02-18', 749.99),
(3, '2023-03-22', 199.99),
(4, '2023-04-12', 1249.98),
(5, '2023-05-05', 299.99),
(6, '2023-06-01', 449.99),
(7, '2023-06-15', 599.98),
(8, '2023-07-08', 199.99),
(9, '2023-07-22', 349.99),
(10, '2023-08-17', 399.99),
(11, '2023-08-25', 749.98),
(12, '2023-09-02', 599.98),
(13, '2023-09-12', 499.99),
(14, '2023-09-20', 899.99),
(15, '2023-09-28', 1099.98),
(16, '2023-10-05', 299.99),
(17, '2023-10-12', 399.99),
(18, '2023-10-22', 999.99),
(19, '2023-11-01', 1299.98),
(20, '2023-11-10', 799.99);
INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate) VALUES
(1, 50, '2024-01-15'),
(2, 30, '2024-01-18'),
(3, 20, '2024-01-20'),
(4, 15, '2024-01-22'),
(5, 10, '2024-01-25'),
(6, 25, '2024-01-28'),
(7, 40, '2024-01-30'),
(8, 60, '2024-02-02'),
(9, 5, '2024-02-05'),
(10, 12, '2024-02-08');
INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES
(2, 1, 2),
(6, 2, 1),
(7, 3, 4),
(8, 4, 3),
(9, 5, 5),
(10, 6, 2),
(11, 7, 1),
(12, 8, 3),
(13, 9, 4),
(14, 10, 2);
/* Adding Categories Attribute to Products Table*/
ALTER TABLE Products
ADD Categories VARCHAR(255);
UPDATE Products 
SET Categories = CASE
 WHEN ProductName IN ('Laptop', 'Tablet', 'Smartphone') THEN 'Electronics'
 WHEN ProductName IN ('Headphones', 'Wireless Mouse', 'Mechanical Keyboard',
'Bluetooth Earbuds') THEN 'Accessories'
 WHEN ProductName = 'Monitor' THEN 'Displays'
 WHEN ProductName = 'External SSD' THEN 'Storage'
 WHEN ProductName = 'Portable Charger' THEN 'Power'
 WHEN ProductName = 'Smart Speaker' THEN 'Smart Home'
 WHEN ProductName = 'Smartwatch' THEN 'Wearables'
 WHEN ProductName = 'VR Headset' THEN 'Gaming'
 WHEN ProductName = 'Gaming Console' THEN 'Gaming'
 WHEN ProductName = 'Smart Home Hub' THEN 'Smart Home'
 WHEN ProductName = 'Drone' THEN 'Drones'
 WHEN ProductName = 'Fitness Band' THEN 'Wearables'
 WHEN ProductName = 'Camera' THEN 'Cameras'
 WHEN ProductName = 'Smart Thermostat' THEN 'Smart Home'
 WHEN ProductName = 'E-reader' THEN 'Electronics'
 ELSE 'Other'
END;
Tasks 2

 / *Write an SQL query to retrieve the names and emails of all customers. */
SELECT FirstName, LastName, Email
FROM customers;
use TECH_SHOP
2. /* Write an SQL query to list all orders with their order dates and corresponding customer 
names. */
 SELECT OrderID,
 OrderDate,
 FirstName + ' ' + LastName AS CustomerName
 FROM
 Orders, Customers
 where
 Orders.CustomerID = Customers.CustomerID;
3. /* Write an SQL query to insert a new customer record into the "Customers" table. Include 
customer information such as name, email, and address. */
INSERT INTO CUSTOMERS (FirstName, LastName , Email, Address)
VALUES('JOHN','SMITH', 'john.doe@gmail.com', '123, siruseri,chennai, india')
4. /* Write an SQL query to update the prices of all electronic gadgets in the "Products" table by 
increasing them by 10%. */
UPDATE Products
SET PRICE = PRICE*1.10
WHERE Categories = 'Electronics';
/* 5. Write an SQL query to delete a specific order and its associated order details from the "Orders" 
and "OrderDetails" tables. Allow users to input the order ID as a parameter. */
 
DECLARE @orderID int = 1;
 DELETE FROM OrderDetails
 WHERE ORDERiD = @orderID;
 
 delete from Orders
 where orderID =@orderID;
select * from Orders;
/* 6. Insert a new order into the "Orders" table. */
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
VALUES (5, '2024-01-15', 1500);
/* 7. Update the contact information of a specific customer in the "Customers" table. */
DECLARE @CustomerID INT;
DECLARE @NewPhone NVARCHAR(20);
DECLARE @NewEmail NVARCHAR(255);
DECLARE @NewAddress NVARCHAR(255);
SET @CustomerID = 21;
SET @NewEmail = 'ACVZ@GMAIL.COM'
SET @NewAddress = '1DQW, WALL STREET, NEW YORK, U.S.A'
SET @NewPhone = '123-456-8490';
UPDATE Customers
SET Email = @NewEmail, Address = @NewAddress, Phone = @NewPhone
WHERE CustomerID = @CustomerID;
/* 8. Recalculate and update the total cost of each order in the "Orders" table. */
UPDATE Orders
SET TotalAmount = (
SELECT SUM(o.TotalAmount * od.Quantity)
FROM OrderDetails od , Orders o
WHERE od.OrderID = Orders.OrderId
)
WHERE EXISTS (
SELECT 1
FROM OrderDetails od
WHERE od.OrderID = Orders.OrderID 
);
/* 9. Delete all orders and their associated order details for a specific customer. */
DECLARE @CustomerID INT = 4;
DELETE FROm OrderDetails
WHERE OrderID IN (
SELECT OrderID FROM Orders WHERE CustomerID = @CustomerID
);
DELETE FROM Orders
WHERE CustomerID = @CustomerID;
select * from OrderDetails
Select * from Orders
/* 10. Insert a new electronic gadget product into the "Products" table. */
SELECT * FROM Products
INSERT INTO Products ( ProductName, Description, Price,Categories)
VALUES ('SAMSUNG', 'OLED TV', 79099.99,'Electronics');
/* 11. Update the status of a specific order in the "Orders" table. */
ALTER TABLE Orders
ADD OrderStatus NVARCHAR(50);
DECLARE @OrderID INT= 6; 
DECLARE @NewStatus NVARCHAR(50) = 'Shipped';
UPDATE Orders
SET OrderStatus = @NewStatus
WHERE OrderID = @OrderID;
/* 12. Calculate and update the number of orders placed by each customer in the "Customers" table. 
*/
ALTER TABLE Customers
ADD OrderCount INT;
SELECT * FROM CUSTOMERS
UPDATE Customers
SET OrderCount = (
SELECT COUNT(*)
FROM Orders
WHERE Orders.CustomerID = Customers.CustomerID
);
Tasks 3
/* 1. Retrieve a list of all orders along with customer information for each order. */
SELECT
 o.OrderID,
 o.OrderDate,
 o.TotalAmount,
 c.CustomerID,
 c. FirstName + ' ' + LastName as Name,
 c.Email,
 c.Address
FROM
 Orders o
JOIN
 Customers c ON o.CustomerID = c.CustomerID
/* 2. Find the total revenue generated by each electronic gadget product. */
SELECT p.ProductName,
 SUM(od.Quantity * p.Price) AS TotalRevenue
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
WHERE p.Categories = 'Electronics' 
GROUP BY p.ProductName;
 /* 3. List all customers who have made at least one purchase. */
 SELECT 
 c.CustomerID,
 c.FirstName + ' ' + LastName 'CUStomer_Name',
 c.Email,
 c.Phone
 FROM
 CUSTOMERS as c
 Join Orders o ON c.CustomerID = o.CustomerID
 Group By
 c.CustomerID, c.FirstName + ' ' + LastName , c.Email, c.Phone;
/* 4. Find the most popular electronic gadget with the highest total quantity ordered. */
SELECT TOP 1 p.ProductName, SUM(od.Quantity) AS TotalQuantityOrdered
FROM Products AS p
JOIN OrderDetails AS od ON p.ProductID = od.ProductID
GROUP BY p.ProductName
ORDER BY SUM(od.Quantity) DESC;
/* 5. Retrieve a list of electronic gadgets along with their corresponding categories. */
SELECT ProductName, Categories
from Products 
Where
Categories = 'Electronics'
/* 6. Calculate the average order value for each customer. */
Select c.FirstName + ' '+ LastName 'CustomerName',
AVG(o.TotalAmount) as AverageOrderValue
FROM
CUSTOMERS c
JOIN Orders o ON c.CustomerID =o.CustomerID
Group BY
c.FirstName + ' '+ LastName;
/* 7. Find the order with the highest total revenue. */
select TOP 1
o.TotalAmount AS TotalRevenue,
c.CustomerID,
o.OrderID,
c.FirstName + ' ' + LastName as CustomerName,
c.Phone
from Orders as o
Join CUSTOMERS as c ON c.CustomerID = o.CustomerID
ORDER BY o.TotalAmount DESC;
/* 8. List electronic gadgets and the number of times each product has been ordered. */
Select p.ProductID, p.ProductName, COUNT(od.OrderID) AS NumberOfOrders
From Products p
Left Join OrderDetails as od ON p.ProductID = od.ProductID
WHERE p.Categories = 'Electronics'
GROUP BY
P.ProductID , p.ProductName
/* 9. Find customers who have purchased a specific electronic gadget product. */
DECLARE @NameOfProduct VARCHAR(255) = 'Electronics'; 
SELECT c.FirstName + ' '+ c.LastName as CustomerName,
c.CustomerID
from CUSTOMERS c
Join Orders as o ON c.CustomerID = o.CustomerID
Join OrderDetails as od ON od.OrderID = o.OrderID
Join Products as p ON p.ProductID = od.ProductID
where p.Categories = @NameOfProduct;
/* 10. Calculate the total revenue generated by all orders placed within a specific time period. */
DECLARE @STARTDATE DATE = '2020-06-01'
DECLARE @ENDDATE DATE = '2024-09-01'
SELECT SUM(TotalAmount ) AS TotalRevenue
From
Orders
Where
OrderDate Between @STARTDATE and @ENDDATE
Tasks 4
/* 1. Find out which customers have not placed any orders. */
Select c.FirstName+' '+c.LastName as NAME 
from CUSTOMERS c
WHERE c.CustomerID NOT IN (SELECT o.CustomerID FROM Orders o )
/* 2. Find the total number of products available for sale. */
SELECT COUNT (*) AS TotalProducts
FROM Products
/* 3. Calculate the total revenue generated by TechShop. */
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders;
/* 4. Calculate the average quantity ordered for products in a specific category. */
DECLARE @CategoryName VARCHAR(255) = 'Electronics';
SELECT AVG(Quantity) AS AverageQuantity
FROM OrderDetails
WHERE ProductID IN (
 SELECT ProductID
 FROM Products
 WHERE Categories = @CategoryName
);
/* 5. Calculate the total revenue generated by a specific customer. */
DECLARE @Customer_ID int=1;
Select Sum(TotalAmount) as TotalRevenueGenerated from Orders
where CustomerID = (Select CustomerID = @Customer_ID)
/* 6. Find the customers who have placed the most orders. */
SELECT top 10
 c.FirstName + ' ' + c.LastName AS Name,
 (
 SELECT COUNT(o.OrderID)
FROM Orders o
WHERE o.CustomerID = c.CustomerID
) AS TotalOrders
FROM
CUSTOMERS c
ORDER BY
TotalOrders DESC;
/* 7. Find the most popular product category with the highest total quantity ordered. */
Select p.ProductName, p.Categories as ProductCategory
from Products as p 
Where p.ProductID = (Select Top 1 od.ProductID 
from OrderDetails od
Group By od.ProductID
Order By SUM(od.Quantity) desc)
/* 8. Find the customer who has spent the most money on electronic gadgets. */
SELECT c.FirstName+' '+ c.LastName as NAME,
SUM(o.TotalAmount) AS TotalSpent
from CUSTOMERS c 
Join Orders o ON o.CustomerID = c.CustomerID
Where o.CustomerID IN
( SELECT TOP 1 o.CustomerID 
from Orders o
where o.OrderID in (
Select od.OrderID 
from OrderDetails od 
Where od.ProductID In (
SELECT p.ProductId 
from Products p 
Where p.Categories = 'Electronics'
)
)
GROUP BY o.CustomerID 
ORder By SUM(o.TotalAmount) DESC
)
GROUP BY c.FirstName + ' '+ c.LastName;
/* 9. Calculate the average order value for all customers. */
SELECT AVG(TotalRevenue/OrderCount) AS AverageOrderValue
From (
Select o.CustomerID,
SUM(o.TotalAmount) AS TotalRevenue,
COUNT(o.OrderID) AS OrderCount
from Orders o
JOIN OrderDetails od ON od.OrderID = o.OrderID
Group By o.CustomerID
) AS OrderSummary
WHERE OrderCount > 0;
/* 10. Find the total number of orders placed by each customer and list their names along with the 
order count. */
select c.FirstName + ' ' + c.LastName as NAME,
(SELECT COUNT(o.OrderID)
FROM Orders o
WHERE o.CustomerID = c.CustomerID)
AS TotalOrders
From CUSTOMERS c
Group By c.CustomerID, c.FirstName,c.LastName
Order BY TotalOrders DESC;