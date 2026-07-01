from app import app
from courses import db
from courses.models import Department, Course, Student, Enrollment

with app.app_context():

    # Clear old data (optional)
    Enrollment.query.delete()
    Course.query.delete()
    Student.query.delete()
    Department.query.delete()

    db.session.commit()

    # Departments
    cs = Department(
        name="Computer Science",
        head_of_dept="Dr. Kumar",
        budget=500000
    )

    it = Department(
        name="Information Technology",
        head_of_dept="Dr. Meena",
        budget=450000
    )

    db.session.add(cs)
    db.session.add(it)
    db.session.commit()

    # Courses
    c1 = Course(
        name="Python Programming",
        code="CS101",
        credits=4,
        department=cs
    )

    c2 = Course(
        name="Database Management",
        code="CS102",
        credits=4,
        department=cs
    )

    c3 = Course(
        name="Computer Networks",
        code="IT201",
        credits=3,
        department=it
    )

    c4 = Course(
        name="Cloud Computing",
        code="IT202",
        credits=4,
        department=it
    )

    db.session.add_all([c1, c2, c3, c4])
    db.session.commit()

    # Students
    s1 = Student(
        first_name="Aswathi",
        last_name="AJ",
        email="aswathi@gmail.com",
        enrollment_year=2024,
        department=cs
    )

    s2 = Student(
        first_name="Rahul",
        last_name="K",
        email="rahul@gmail.com",
        enrollment_year=2024,
        department=cs
    )

    s3 = Student(
        first_name="Anu",
        last_name="S",
        email="anu@gmail.com",
        enrollment_year=2024,
        department=it
    )

    s4 = Student(
        first_name="Priya",
        last_name="M",
        email="priya@gmail.com",
        enrollment_year=2024,
        department=it
    )

    s5 = Student(
        first_name="Arun",
        last_name="R",
        email="arun@gmail.com",
        enrollment_year=2024,
        department=cs
    )

    db.session.add_all([s1, s2, s3, s4, s5])
    db.session.commit()

    # Enrollments
    e1 = Enrollment(student=s1, course=c1)
    e2 = Enrollment(student=s2, course=c2)
    e3 = Enrollment(student=s3, course=c3)
    e4 = Enrollment(student=s4, course=c4)

    db.session.add_all([e1, e2, e3, e4])
    db.session.commit()

    print("Sample data inserted successfully!")