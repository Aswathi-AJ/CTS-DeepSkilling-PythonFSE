use college_db;

-- TASK 1

select s.student_id ,s.first_name,s.last_name
from students s join enrollments e
on s.student_id=e.student_id
group by s.student_id,s.first_name,s.last_name
having count(*)>
(
select avg(total_courses)
from(select student_id,count(*) as total_courses 
from enrollments group by student_id
)t
);

select c.course_id, c.course_name
from courses c
where not exists
(
select * from enrollments e
where e.course_id = c.course_id
and e.grade <> 'A'
);

select p.prof_name,p.salary,p.department_id
from professors p
where p.salary =
(
select max(p2.salary)from professors p2
where p2.department_id = p.department_id
);

select * from
(
select department_id, avg(salary) as avg_salary
from professors
group by department_id
)dept_avg
where avg_salary > 85000;

-- TASK 2

create view vw_student_enrollment_summary as
select s.student_id,concat(s.first_name,' ',s.last_name) as student_name,d.department_name,count(e.course_id) as total_courses,
round(avg(
case
when e.grade='A' then 4
when e.grade='B' then 3
when e.grade='C' then 2
when e.grade='D' then 1
when e.grade='F' then 0
end
),2) as gpa
from students s join departments d
on s.department_id=d.department_id
left join enrollments e
on s.student_id=e.student_id
group by s.student_id,student_name,d.department_name;
select * from vw_student_enrollment_summary;

create view vw_course_stats as
select c.course_name,c.course_code,count(e.student_id)as total_enrollments,
round(avg(
case
when e.grade='A' then 4
when e.grade='B' then 3
when e.grade='C' then 2
when e.grade='D' then 1
when e.grade='F' then 0
end
),2) as avg_gpa
from courses c left join enrollments e
on c.course_id=e.course_id
group by c.course_id,c.course_name,c.course_code;
select * from vw_course_stats;

select * from vw_student_enrollment_summary 
where gpa >3.0;

update vw_student_enrollment_summary 
set gpa = 4.0 
where student_id = 1;
/*
The view vw_student_enrollment_summary is not updatable because it contains:
- Multiple joined tables
- Aggregate functions (COUNT, AVG)
- GROUP BY
- Derived calculated columns
MySQL cannot determine how changes should be propagated back to the underlying tables.
Therefore the UPDATE operation fails.
*/

drop view vw_student_enrollment_summary;
drop view vw_course_stats;
create view vw_student_enrollment_summary as
select student_id,first_name,last_name,enrollment_year
from students
where enrollment_year >= 2023
with check option;

-- TASK 3

delimiter $$
create procedure sp_enroll_student(
in p_student_id int,
in p_course_id int,
in p_enrollment_date date
)
begin
if exists
(
select 1 
from enrollments
where student_id = p_student_id
and course_id = p_course_id
)
then
signal sqlstate '45000'
set message_text='Student already enrolled in this course';
else
insert into enrollments(student_id,course_id,enrollment_date)values
(p_student_id,p_course_id,p_enrollment_date);
end if;
end $$
delimiter ;
call sp_enroll_student(9,1,'2024-01-10');

create table department_transfer_log(
log_id int auto_increment primary key,
student_id int,
old_department_id int,
new_department_id int,
transfer_date timestamp default current_timestamp
);
delimiter $$
create procedure sp_transfer_student(
in p_student_id int,
in p_new_department_id int
)
begin
declare v_old_department int;
start transaction;
select department_id into v_old_department
from students
where student_id = p_student_id;
update students
set department_id = p_new_department_id
where student_id = p_student_id;
insert into department_transfer_log(student_id,old_department_id,new_department_id)values
(p_student_id,v_old_department,p_new_department_id);
commit;
end $$
delimiter ;

call sp_transfer_student(1,999);
-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`college_db`.`students`, CONSTRAINT `students_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`))

start transaction;

insert into enrollments(student_id,course_id,enrollment_date)values
(9,2,'2024-01-01');
savepoint first_insert;
insert into enrollments(student_id,course_id,enrollment_date)values
(999,2,'2024-01-01');
-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`college_db`.`enrollments`, CONSTRAINT `enrollments_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`))
rollback to first_insert;
commit;