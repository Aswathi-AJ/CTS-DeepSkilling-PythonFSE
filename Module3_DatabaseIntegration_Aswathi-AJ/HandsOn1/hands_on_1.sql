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

insert into departments (department_name, hod_name, budget) values
('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
('Electronics', 'Dr. Priya Nair', 620000.00),
('Mechanical', 'Dr. Suresh Iyer', 540000.00),
('Civil', 'Dr. Ananya Sharma', 430000.00);
select * from departments;

insert into students (first_name, last_name, email, date_of_birth, department_id,enrollment_year) values
('Arjun', 'Mehta', 'arjun.mehta@college.edu', '2003-04-12', 1, 2022),
('Priya', 'Suresh', 'priya.suresh@college.edu', '2003-07-25', 1, 2022),
('Rohan', 'Verma', 'rohan.verma@college.edu', '2002-11-08', 2, 2021),
('Sneha', 'Patel', 'sneha.patel@college.edu', '2004-01-30', 3, 2023),
('Vikram', 'Das', 'vikram.das@college.edu', '2003-09-14', 1, 2022),
('Kavya', 'Menon', 'kavya.menon@college.edu', '2002-05-17', 2, 2021),
('Aditya', 'Singh', 'aditya.singh@college.edu', '2004-03-22', 4, 2023),
('Deepika','Rao', 'deepika.rao@college.edu', '2003-08-09', 1, 2022);
select * from students;

insert into courses (course_name, course_code, credits, department_id) values
('Data Structures & Algorithms', 'CS101', 4, 1),
('Database Management Systems', 'CS102', 3, 1),
('Object Oriented Programming', 'CS103', 4, 1),
('Circuit Theory', 'EC101', 3, 2),
('Thermodynamics', 'ME101', 3, 3);
select * from courses;

insert into enrollments (student_id, course_id, enrollment_date, grade) values
(1, 1, '2022-07-01', 'A'), (1, 2, '2022-07-01', 'B'),
(2, 1, '2022-07-01', 'B'), (2, 3, '2022-07-01', 'A'),
(3, 4, '2021-07-01', 'A'), (4, 5, '2023-07-01', NULL),
(5, 1, '2022-07-01', 'C'), (5, 2, '2022-07-01', 'A'),
(6, 4, '2021-07-01', 'B'), (7, 5, '2023-07-01', NULL),
(8, 1, '2022-07-01', 'A'), (8, 3, '2022-07-01', 'B');
select * from enrollments;

insert into professors (prof_name, email, department_id, salary) values
('Dr. Anand Krishnan', 'anand.k@college.edu', 1, 95000.00),
('Dr. Meena Pillai', 'meena.p@college.edu', 1, 88000.00),
('Dr. Sunil Rajan', 'sunil.r@college.edu', 2, 82000.00),
('Dr. Latha Gopal', 'latha.g@college.edu', 3, 79000.00),
('Dr. Kartik Bose', 'kartik.b@college.edu', 4, 76000.00);
select * from professors;

select count(*) from departments;
select count(*) from students;
select count(*) from courses;
select count(*) from enrollments;
select count(*) from professors;

/*
Normalization Verification

1NF:
- All tables contain atomic values.
- No column stores multiple values in a single cell.

2NF:
- All non-key attributes depend on the entire primary key.
- Student information is separated from enrollment information.

3NF:
- No transitive dependencies exist.
- Department information is stored only in the departments table.
- Students, Courses, and Professors reference departments using department_id.
- Redundant department data is avoided.
*/