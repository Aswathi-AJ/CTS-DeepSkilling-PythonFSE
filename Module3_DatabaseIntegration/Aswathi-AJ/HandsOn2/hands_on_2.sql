USE college_db;

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

insert into students (first_name, last_name, email, date_of_birth, department_id,enrollment_year) values
('Meera', 'krishnan', 'meera.k@college.edu', '2006-05-22', 1, 2022),
('Aswathi', 'aj', 'aswathi.aj@college.edu', '2006-03-23', 1, 2021);
select count(*) from students;

update enrollments set grade='B' where student_id = 5 and course_id = 1;
select count(*) from enrollments;

select * from enrollments where grade is null;
set sql_safe_updates=0;
delete from enrollments where grade is null;