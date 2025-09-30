create database companydb;
use companydb;

create table Departments(
dept_id int auto_increment primary key,
dept_name varchar(50) not null
);

create table Employees (
	emp_id int auto_increment primary key,
    name varchar(50) ,
    age int,
    salary decimal(10,2),
    dept_id int,
    foreign key(dept_id) references Departments(dept_id)
    );

insert into departments (dept_name) values
('IT'),
('HR'),
('Finance'),
('Sales');

INSERT INTO Employees (name, age, salary, dept_id) VALUES
('Rahul', 28, 55000, 1),   -- IT
('Priya', 32, 60000, 2),   -- HR
('Arjun', 25, 48000, 3),   -- Finance
('Neha', 30, 70000, 1),    -- IT
('Vikram', 35, 65000, 4);  -- Sales

TRUNCATE TABLE Employees;
    SET FOREIGN_KEY_CHECKS = 0;
    TRUNCATE TABLE Departments;
    SET FOREIGN_KEY_CHECKS = 1;
    
    INSERT INTO Departments (dept_name) VALUES
('IT'),         -- id = 1
('HR'),         -- id = 2
('Finance'),    -- id = 3
('Sales'),      -- id = 4
('Marketing');  -- id = 5  

INSERT INTO Employees (name, age, salary, dept_id) VALUES

('Rahul', 28, 55000, 1),   -- IT

('Priya', 32, 60000, 2),   -- HR

('Arjun', 25, 48000, NULL),-- 

('Neha', 30, 70000, 1),    -- IT

('Vikram', 35, 65000, 4);  -- Sales

select e.name , e.salary , d.dept_name
from employees e
inner join departments d
on e.dept_id = d.dept_id 

select e.name , e.salary , d.dept_name
from employees e
left join departments d
on e.dept_id = d.dept_id 

select e.name , e.salary , d.dept_name
from employees e
right join departments d
on e.dept_id = d.dept_id 

select e.name , e.salary , d.dept_name
from employees e
left join departments d
on e.dept_id = d.dept_id 
union
select e.name , e.salary , d.dept_name
from employees e
right join departments d
on e.dept_id = d.dept_id 

  
    create table teachers (
    teacher_id int auto_increment primary key,
    name varchar(50),
    subject_id int);
    
    create table subjects (
    subject_id int auto_increment primary key,
    subject_name varchar(50)
    );
    
    INSERT INTO Subjects (subject_name) VALUES
('Mathematics'),   -- id = 1
('Science'),       -- id = 2
('English'),       -- id = 3
('History'),       -- id = 4
('Geography');     -- id = 5 (no teacher yet)

INSERT INTO Teachers (name, subject_id) VALUES
('Rahul Sir', 1),   -- Mathematics
('Priya Madam', 2), -- Science
('Arjun Sir', NULL),-- No subject assigned
('Neha Madam', 3);  -- English

select t.name , s.subject_name
from teachers t
left join subjects s
on t.subject_id= s.subject_id ;

select t.name , s.subject_name
from teachers t
right join subjects s
on t.subject_id= s.subject_id ;

select t.name , s.subject_name
from teachers t
left join subjects s
on t.subject_id= s.subject_id ;
union
select t.name , s.subject_name
from teachers t
right join subjects s
on t.subject_id= s.subject_id ;