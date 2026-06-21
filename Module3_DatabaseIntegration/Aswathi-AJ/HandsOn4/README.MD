# Hands-On 4 - Query Optimisation, Indexes & N+1 Problem

## Task 1: Baseline Performance

* Used EXPLAIN FORMAT=JSON to analyze query execution plans.
* Identified Full Table Scan on the students table.
* Examined query cost and rows examined.

## Task 2: Indexes and Query Plans

* Created an index on students.enrollment_year.
* Created a composite UNIQUE index on enrollments(student_id, course_id).
* Created an index on courses.course_code.
* Compared execution plans before and after indexing.

## Task 3: N+1 Query Problem

* Simulated the N+1 query problem using Python and MySQL.
* Measured the number of queries executed.
* Rewrote the solution using a JOIN query.
* Compared execution time and database round-trips.
* Studied the impact of N+1 queries on application performance.

## Concepts Practiced

* Query Optimization
* EXPLAIN FORMAT=JSON
* Full Table Scan
* Indexes
* Composite UNIQUE Indexes
* Query Plans
* N+1 Problem
* JOIN Optimization

## Status

Hands-On 4 Completed.
