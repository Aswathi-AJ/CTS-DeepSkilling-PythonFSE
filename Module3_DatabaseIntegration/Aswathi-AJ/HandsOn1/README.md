# Hands-On 1 - Database Integration

## Student Course Registration System

### Tasks Completed

#### Task 1: Database Schema Creation

* Created `college_db`
* Created `departments` table
* Created `students` table
* Created `courses` table
* Created `enrollments` table
* Created `professors` table

#### Task 2: Data Insertion and Normalization

* Inserted sample data into all tables
* Verified data insertion
* Analyzed schema for 1NF, 2NF, and 3NF compliance

#### Task 3: Alter and Extend Schema

* Added `phone_number` column to students
* Added `max_seats` column to courses with default value
* Added CHECK constraint on grades
* Renamed `hod_name` to `head_of_dept`
* Dropped `phone_number` column to simulate rollback
* Verified changes using `DESCRIBE` and `INFORMATION_SCHEMA.COLUMNS`

### Concepts Practiced

* DDL Commands
* CREATE DATABASE
* CREATE TABLE
* ALTER TABLE
* PRIMARY KEY
* FOREIGN KEY
* UNIQUE Constraint
* CHECK Constraint
* DEFAULT Constraint
* Data Normalization (1NF, 2NF, 3NF)
* Schema Verification

### Status

Hands-On 1 completed up to Task 3.
