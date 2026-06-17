-- Student Course Registration System

CREATE DATABASE college_db;
USE college_db;

create table departments(
department_id INT auto_increment PRIMARY KEY,
department_name VARCHAR(100) NOT NULL,
hod_name VARCHAR(100),
budget DECIMAL(12,2)
);
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

/* 
Normalization Analysis

1NF Compliance:
- All tables contain atomic values only.
- No column stores multiple values in a single cell.
- Each row-column intersection contains exactly one value.

2NF Compliance:
- All tables are in 1NF.
- Non-key attributes are fully dependent on their primary keys.
- Student information is separated from enrollment information to avoid partial dependency.

3NF Compliance:
- All tables are in 2NF.
- No transitive dependencies exist between non-key attributes.
- Department details are stored only in the departments table.
- Students, Courses, and Professors reference departments through department_id.
- Data redundancy is minimized and update anomalies are avoided.
*/

alter table students
add column phone_number varchar(15);
describe students;

alter table courses
add column max_seats int default 60;
select column_name, data_type
from information_schema.columns
where table_schema = 'college_db'
and table_name = 'courses';

alter table enrollments
add constraint chk_grade
check (grade in ('A','B','C','D','F') or grade is null);
insert into enrollments(student_id, course_id, enrollment_date, grade)values
(1,1,'2024-01-01','X');
-- Error Code: 3819. Check constraint 'chk_grade' is violated.

alter table departments
change hod_name head_of_dept varchar(100);
select column_name
from information_schema.columns
where table_schema = 'college_db'
and table_name = 'departments';

alter table students
drop column phone_number;
select column_name
from information_schema.columns
where table_schema = 'college_db'
and table_name = 'students';