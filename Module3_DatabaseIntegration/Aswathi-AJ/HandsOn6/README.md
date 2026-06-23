# HandsOn 6 – SQLAlchemy ORM Integration

## Objective

Learn SQLAlchemy ORM by mapping MySQL tables to Python classes and performing CRUD operations.

## Files

* `models.py` – Database connection, ORM models, relationships
* `crud.py` – CRUD operations and query optimization examples
* `.env` – Database credentials

## Tasks Completed

### Task 1 – ORM Model Definition

* Created SQLAlchemy Engine
* Defined Base class
* Created ORM models:

  * Department
  * Student
  * Professor
  * Course
  * Enrollment
* Added relationships using `relationship()`
* Used `Base.metadata.create_all()`

### Task 2 – CRUD Operations

* Inserted Departments and Students
* Inserted Courses and Enrollments
* Read data using ORM queries
* Updated student records
* Deleted enrollment records

### Task 3 – Query Optimization

* Identified N+1 Query Problem
* Implemented eager loading using `joinedload()`
* Reduced multiple SQL queries to a single optimized query
* Compared lazy loading and eager loading approaches



