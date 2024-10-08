CREATE DATABASE OrderManagement;

use OrderManagement;

CREATE TABLE Users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(100) NOT NULL,
    password NVARCHAR(100) NOT NULL,
    role NVARCHAR(10) CHECK(role IN ('Admin', 'User'))
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY IDENTITY(1,1),
    product_name NVARCHAR(100) NOT NULL,
    description NVARCHAR(255),
    price DECIMAL(10, 2),
    quantity_in_stock INT,
    type NVARCHAR(15) CHECK(type IN ('Electronics', 'Clothing')), -- Adjusted size
    brand NVARCHAR(100),
    warranty_period INT,
    size NVARCHAR(10),
    color NVARCHAR(20)
);
;

CREATE TABLE Orders (
    order_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    product_id INT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id	),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
);


select * from Products
select * from Users;
select * from Orders

-- Inserting  15 rows of data for each table
-- Users table 
INSERT INTO Users (username, password, role) VALUES 
('admin1', 'password1', 'Admin'),
('admin2', 'password2', 'Admin'),
('user1', 'password3', 'User'),
('user2', 'password4', 'User'),
('user3', 'password5', 'User'),
('user4', 'password6', 'User'),
('user5', 'password7', 'User'),
('user6', 'password8', 'User'),
('user7', 'password9', 'User'),
('user8', 'password10', 'User'),
('user9', 'password11', 'User'),
('user10', 'password12', 'User'),
('admin3', 'password13', 'Admin'),
('user11', 'password14', 'User'),
('admin4', 'password15', 'Admin');

-- Inserting into Products table
INSERT INTO Products (product_name, description, price, quantity_in_stock, type, brand, warranty_period, size, color) VALUES
('Smartphone', 'Latest model smartphone', 699.99, 100, 'Electronics', 'BrandX', 24, NULL, NULL),
('Laptop', 'High performance laptop', 1299.99, 50, 'Electronics', 'BrandY', 36, NULL, NULL),
('Television', '4K Ultra HD TV', 899.99, 20, 'Electronics', 'BrandZ', 12, NULL, NULL),
('T-Shirt', 'Cotton T-shirt', 19.99, 200, 'Clothing', NULL, NULL, 'L', 'Red'),
('Jeans', 'Denim jeans', 49.99, 150, 'Clothing', NULL, NULL, '32', 'Blue'),
('Sweater', 'Woolen sweater', 39.99, 100, 'Clothing', NULL, NULL, 'M', 'Green'),
('Headphones', 'Noise-canceling headphones', 199.99, 80, 'Electronics', 'BrandA', 12, NULL, NULL),
('Watch', 'Smartwatch with fitness tracking', 299.99, 60, 'Electronics', 'BrandB', 18, NULL, NULL),
('Shirt', 'Formal shirt', 29.99, 100, 'Clothing', NULL, NULL, 'M', 'White'),
('Jacket', 'Leather jacket', 129.99, 50, 'Clothing', NULL, NULL, 'L', 'Black'),
('Microwave', 'Convection microwave', 99.99, 40, 'Electronics', 'BrandC', 24, NULL, NULL),
('Blender', 'High-speed blender', 59.99, 30, 'Electronics', 'BrandD', 18, NULL, NULL),
('Shoes', 'Running shoes', 79.99, 120, 'Clothing', NULL, NULL, '9', 'Black'),
('Camera', 'DSLR camera', 499.99, 25, 'Electronics', 'BrandE', 24, NULL, NULL),
('Socks', 'Cotton socks', 9.99, 300, 'Clothing', NULL, NULL, 'One size', 'Gray');


-- Inserting into Orders table
INSERT INTO Orders (user_id, product_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15);

