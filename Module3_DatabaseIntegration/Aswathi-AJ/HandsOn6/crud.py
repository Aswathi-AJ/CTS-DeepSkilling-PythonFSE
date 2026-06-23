# TASK 2

from asyncio import Task
from sqlalchemy.orm import sessionmaker
from models import engine
Session = sessionmaker(bind=engine)
session = Session()
print("Session Created Successfully")


from models import Department, Student
from datetime import date
dept1 = Department(
    department_id=5,
    department_name="AI",
    head_of_dept="Dr. Kumar",
    budget=500000
)
dept2 = Department(
    department_id=6,
    department_name="Cyber Security",
    head_of_dept="Dr. Priya",
    budget=600000
)
dept3 = Department(
    department_id=7,
    department_name="Data Science",
    head_of_dept="Dr. Ravi",
    budget=700000
)
student1 = Student(
    student_id=11,
    first_name="Anu",
    last_name="Raj",
    email="anu@gmail.com",
    date_of_birth=date(2005, 5, 10),
    enrollment_year=2025,
    department_id=5
)
student2 = Student(
    student_id=12,
    first_name="Hari",
    last_name="Krish",
    email="hari@gmail.com",
    date_of_birth=date(2005, 3, 15),
    enrollment_year=2025,
    department_id=5
)
student3 = Student(
    student_id=13,
    first_name="Nila",
    last_name="Devi",
    email="nila@gmail.com",
    date_of_birth=date(2004, 11, 20),
    enrollment_year=2025,
    department_id=6
)
student4 = Student(
    student_id=14,
    first_name="Arav",
    last_name="Mohan",
    email="arav@gmail.com",
    date_of_birth=date(2005, 1, 5),
    enrollment_year=2025,
    department_id=7
)
student5 = Student(
    student_id=15,
    first_name="Megha",
    last_name="Raj",
    email="megha@gmail.com",
    date_of_birth=date(2004, 9, 18),
    enrollment_year=2025,
    department_id=7
)
session.add_all([
    dept1, dept2, dept3,
    student1, student2, student3,student4, student5
])
session.commit()
print("Completed Successfully")


from models import Course, Enrollment
course1 = Course(
    course_id=6,
    course_code="AI101",
    course_name="Introduction to AI",
    credits=3,
    department_id=5
)
course2 = Course(
    course_id=7,
    course_code="CS201",
    course_name="Ethical Hacking",
    credits=4,
    department_id=6
)
course3 = Course(
    course_id=8,
    course_code="DS301",
    course_name="Machine Learning",
    credits=4,
    department_id=7
)
enrollment1 = Enrollment(
    enrollment_id=15,
    student_id=11,
    course_id=6,
    enrollment_date=date(2025, 1, 10),
    grade="A"
)
enrollment2 = Enrollment(
    enrollment_id=16,
    student_id=12,
    course_id=6,
    enrollment_date=date(2025, 1, 10),
    grade="B"
)
enrollment3 = Enrollment(
    enrollment_id=17,
    student_id=13,
    course_id=7,
    enrollment_date=date(2025, 1, 12),
    grade="A"
)
enrollment4 = Enrollment(
    enrollment_id=18,
    student_id=14,
    course_id=8,
    enrollment_date=date(2025, 1, 15),
    grade="A"
)
session.add_all([
    course1,course2,course3,
    enrollment1,enrollment2,enrollment3,enrollment4
])
session.commit()


enrollments = session.query(Enrollment).all()
print("\nEnrollment Details:\n")
for enrollment in enrollments:
    print(
        f"{enrollment.student.first_name} "
        f"{enrollment.student.last_name}"
        f" -> "
        f"{enrollment.course.course_name}"
    )


student = (
    session.query(Student)
    .filter(Student.email == "anu@gmail.com")
    .first()
)
if student:
    student.enrollment_year = 2026
    session.commit()
    print("Student Updated Successfully")


enrollment = (
    session.query(Enrollment)
    .filter(Enrollment.enrollment_id == 18)
    .first()
)
if enrollment:
    session.delete(enrollment)
    session.commit()
    print("Enrollment Deleted Successfully")

"""
Expected Outcome:
Echo logs show multiple SQL statements being executed.
This indicates the N+1 Query Problem, where one query loads
enrollments and additional queries load related student and
course records.
"""


# TASK 3
"""
N+1 Query Problem Observed
Query 1:Loads all enrollments.
Additional queries:Load related student records.
Additional queries:Load related course records.
Approximate query count:13 queries.
"""


from sqlalchemy.orm import joinedload
enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)
for enrollment in enrollments:
    print(
        f"{enrollment.student.first_name} "
        f"{enrollment.student.last_name}"
        f" -> "
        f"{enrollment.course.course_name}"
    )


# Question 89
"""
After joinedload():
Enrollment
Student
Course

loaded together.
Approximate query count:1 query.
"""


#Question 90
"""
N+1 Query Comparison

Before joinedload():
- Approx. 13 SQL queries
- One query for enrollments
- Additional queries for student/course data
After joinedload():
- Approx. 1 SQL query
- Enrollment, Student and Course data
  loaded together using JOINs

Performance improved significantly.
"""


# Question 91
"""
Django ORM Equivalent:
Enrollment.objects.select_related(
    'student',
    'course'
).all()

SQLAlchemy Equivalent:
session.query(Enrollment).options(
    joinedload(Enrollment.student),
    joinedload(Enrollment.course)
).all()
"""