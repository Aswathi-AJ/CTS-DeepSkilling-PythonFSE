-- Student Course Registration System

CREATE DATABASE college_db;
USE college_db;

create table departments(
department_id INT auto_increment PRIMARY KEY,
department_name VARCHAR(100) NOT NULL,
hod_name VARCHAR(100),
budget DECIMAL(12,2)
);
SHOW TABLES;
DESCRIBE departments;

create table students(
student_id int auto_increment primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(100) unique not null,
date_of_birth date,
department_id int,
enrollment_year int,
foreign key(department_id)references departments(department_id)
);
describe students;
        
create table courses (
course_id int auto_increment primary key,
course_name varchar(150) not null,
course_code varchar(20) unique,
credits int,
department_id int,
foreign key (department_id)references departments(department_id)
);
describe courses;

create table enrollments(
enrollment_id int auto_increment primary key,
student_id int,
course_id int,
enrollment_date date,
grade char(2),
foreign key (student_id)references students(student_id),
foreign key (course_id)references courses(course_id)
);
describe enrollments;

create table professors (
professor_id int auto_increment primary key,
prof_name varchar(100) not null,
email varchar(100) unique,
department_id int,
salary decimal(10,2),
foreign key (department_id)references departments(department_id)
);
describe professors;

show tables;