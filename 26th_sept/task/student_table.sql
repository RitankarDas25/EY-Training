create database SchoolDB;

use SchoolDB;


create table Students (
	id int auto_increment primary key,
    name varchar(50),
    age int,
    course varchar(50),
    marks int
    );
    
    insert into students (name, age , course , marks)
    values ('Rahul',21,'AI',85);
    
    insert into students (name, age , course , marks)
    values ('Priya',22,'ML',90),
     ('Abhi',23,'ML',90);
     delete from students where name = "Abhi";
     select * from students;
     
     select name,marks from students;
     
     select name,marks from students where marks>85;
     
     update students
     set marks=95 where id =2;
    