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
