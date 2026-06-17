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
