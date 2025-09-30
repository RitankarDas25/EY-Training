create database if not exists retailnf;
use retailnf;

create table BadOrders (
order_id int primary key,
order_date date,
customer_id int,
customer_name varchar(50),
customer_city varchar(50),
-- repeating groups (comma separated)
product_ids varchar(200),
product_names varchar(200),
unit_prices varchar(200),
quantities varchar(200),
order_total decimal(10,2) -- derivable sum
);

INSERT INTO BadOrders VALUES
-- order_id, date, cust, name, city,     pids,      pnames,                   prices,        qtys,    total
(101, '2025-09-01', 1, 'Rahul', 'Mumbai', '1,3',    'Laptop,Headphones',      '60000,2000',  '1,2',   64000.00),
(102, '2025-09-02', 2, 'Priya', 'Delhi',  '2',      'Smartphone',             '30000',       '1',     30000.00);

create table orders_1nf (
order_id int primary key,
order_date date,
customer_id int,
customer_name varchar(50),
customer_city varchar(50)
);

create table order_items_1nf(
order_id int,
line_no int,
product_ids int,
product_names varchar(200),
unit_prices decimal(10,2),
quantities int,
primary key (order_id , line_no),
foreign key (order_id) references orders_1nf(order_id)
);

insert into orders_1nf
select order_id, order_date,customer_id,customer_name, customer_city
from Badorders;

insert into order_items_1nf values
(101,1,1,'laptop',60000,1),
(101,2,3,'headphones',2000,2),
(102,1,2,'smartphone',30000,1);

-- 3NF
create table customers_2NF (
customer_id int primary key,
customer_name varchar(50),
customer_city varchar(50)
);

create table orders_2nf
(
order_id int primary key,
order_date date,
customer_id int,
foreign key (customer_id) references customers_2nf(customer_id)
);

create table products_2nf (
product_id int primary key,
product_name varchar(50),
category varchar(50),
list_price decimal(10,2)
);

CREATE TABLE OrderItems_2NF (
  order_id INT,
  line_no INT,
  product_id INT,
  unit_price_at_sale DECIMAL(10,2),  -- historical price
  quantity INT,
  PRIMARY KEY (order_id, line_no),
  FOREIGN KEY (order_id) REFERENCES Orders_2NF(order_id),
  FOREIGN KEY (product_id) REFERENCES Products_2NF(product_id)
);

-- Seed dimension tables (from what we saw in BadOrders/OrderItems_1NF)
INSERT INTO Customers_2NF VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Priya', 'Delhi');
 
INSERT INTO Products_2NF VALUES
(1, 'Laptop',     'Electronics', 60000),
(2, 'Smartphone', 'Electronics', 30000),
(3, 'Headphones', 'Accessories',  2000);
 
INSERT INTO Orders_2NF VALUES
(101, '2025-09-01', 1),
(102, '2025-09-02', 2);
 
INSERT INTO OrderItems_2NF VALUES
(101, 1, 1, 60000, 1),
(101, 2, 3,  2000, 2),
(102, 1, 2, 30000, 1);

-- 3NF
CREATE TABLE Cities (
city_id INT PRIMARY KEY,
city_name VARCHAR (50),
state VARCHAR (50)
);
 
CREATE TABLE Customers_3NF (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
city_id INT,
FOREIGN KEY (city_id) REFERENCES Cities(city_id)
) ;
 
-- Carry over Orders / Products / OrderItems to 3NF naming
CREATE TABLE Products_3NF LIKE Products_2NF;
INSERT INTO Products_3NF SELECT * FROM Products_2NF;
 
CREATE TABLE Orders_3NF LIKE Orders_2NF;
CREATE TABLE OrderItems_3NF LIKE OrderItems_2NF;
 
-- Seed Cities + Customers (Mumbai - Maharashtra, Delhi - Delhi)
INSERT INTO Cities VALUES
(10, 'Mumbai', 'Maharashtra'),
(20, 'Delhi', 'Delhi') ;
 
INSERT INTO Customers_3NF VALUES
(1, 'Rahul', 10),
(2, 'Priya', 20);
 
INSERT INTO Orders_3NF SELECT * FROM Orders_2NF;
INSERT INTO OrderItems_3NF SELECT * FROM OrderItems_2NF;