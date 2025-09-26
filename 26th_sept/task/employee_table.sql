use SchoolDB;
create table Employees (
	id int auto_increment primary key,
    name varchar(50) not null,
    age int,
    department varchar(50),
    salary decimal(10,2)
    );
    
    insert into Employees (name, age , department , salary)
    values ('Rahul',21,'AI',85000.00),
			('Riya',21,'hr',60000.00),
		('yash',21,'sde',50000.00);
      select * from employees;
	select name,department from employees where salary>50000.00;
   UPDATE employees
SET salary = 90000
WHERE id = 1 AND department = 'AI';

     select * from employees;
     delete from employees where id=3 and name = "yash";
     select * from employees;
     
  
     
 
     
     