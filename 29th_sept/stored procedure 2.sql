create database RetailDB;
use RetailDB;

create table customers (
customer_id int auto_increment primary key,
name varchar(50),
city varchar(50),
phone varchar(15)
);

create table products (
product_id int auto_increment primary key,
product_name varchar(50),
category varchar(50),
price decimal(10,2)
);

create table orders (
order_id int auto_increment primary key,
customer_id int,
order_date date,
foreign key (customer_id) references customers(customer_id)
);

create table orderdetails (
order_detail_id int auto_increment primary key,
order_id int,
product_id int,
quantity int,
foreign key (order_id) references orders(order_id),
foreign key (product_id) references products(product_id)
);

INSERT INTO Customers (name, city, phone) VALUES
('Rahul', 'Mumbai', '9876543210'),
('Priya', 'Delhi', '9876501234'),
('Arjun', 'Bengaluru', '9876512345'),
('Neha', 'Hyderabad', '9876523456');


INSERT INTO Products (product_name, category, price) VALUES
('Laptop', 'Electronics', 60000.00),
('Smartphone', 'Electronics', 30000.00),
('Headphones', 'Accessories', 2000.00),
('Shoes', 'Fashion', 3500.00),
('T-Shirt', 'Fashion', 1200.00);


INSERT INTO Orders (customer_id, order_date) VALUES
(1, '2025-09-01'),
(2, '2025-09-02'),
(3, '2025-09-03'),
(1, '2025-09-04');


INSERT INTO OrderDetails (order_id, product_id, quantity) VALUES
(1, 1, 1),   -- Rahul bought 1 Laptop
(1, 3, 2),   -- Rahul bought 2 Headphones
(2, 2, 1),   -- Priya bought 1 Smartphone
(3, 4, 1),   -- Arjun bought 1 Shoes
(4, 5, 3);   -- Rahul bought 3 T-Shirts

DELIMITER $$
CREATE PROCEDURE GetAllProducts()
BEGIN
    SELECT product_id, product_name, category, price
    FROM products;
END$$
DELIMITER ;

call GetAllProducts();

DELIMITER $$
CREATE PROCEDURE GetOrdersWithCustomers()
BEGIN
    SELECT o.order_id , o.order_date , c.name As customer_name
    FROM orders o
    join customers c
    on o.customer_id = c.customer_id;
END$$
DELIMITER ;

call GetOrderswithCustomers();

DELIMITER $$
CREATE PROCEDURE GetFullOrdersDetails()
BEGIN
    SELECT o.order_id ,  c.name As customer_name , p.product name,
    od.quantity,
    p.price,
    (od.quantity * p.price) as total
    FROM orders o
    join customers c 
    on o.customer_id = c.customer_id
    join orderdetails od on o.order_id = od.order_id
    join products p on od.product_id = p.product_id;
END$$
DELIMITER ;

call GetFullOrdersDetails();

DELIMITER $$
CREATE PROCEDURE GettopProducts()
BEGIN
    SELECT p.product_name, sum(od.quantity) as total_sold,
    sum(od.quantity*p.price) as revenue
    
    FROM orderdetails od 
    join products p on od.product_id = p.product_id
    group by p.product_id , p.product_name
    order by revenue desc
    limit 3;
END$$
DELIMITER ;

call GetTopProducts();

