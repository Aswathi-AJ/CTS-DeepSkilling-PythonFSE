use college_db;

-- TASK 1

explain format=json
select s.first_name,s.last_name,c.course_name
from enrollments e join students s
on s.student_id = e.student_id
join courses c
on c.course_id = e.course_id
where s.enrollment_year = 2022;
/* {
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "2.45"
    },
    "nested_loop": [
      {
        "table": {
          "table_name": "s",
          "access_type": "ALL",
          "possible_keys": [
            "PRIMARY"
          ],
          "rows_examined_per_scan": 10,
          "rows_produced_per_join": 1,
          "filtered": "10.00",
          "cost_info": {
            "read_cost": "1.15",
            "eval_cost": "0.10",
            "prefix_cost": "1.25",
            "data_read_per_join": "824"
          },
          "used_columns": [
            "student_id",
            "first_name",
            "last_name",
            "enrollment_year"
          ],
          "attached_condition": "(`college_db`.`s`.`enrollment_year` = 2022)"
        }
      },
      {
        "table": {
          "table_name": "e",
          "access_type": "ref",
          "possible_keys": [
            "student_id",
            "course_id"
          ],
          "key": "student_id",
          "used_key_parts": [
            "student_id"
          ],
          "key_length": "5",
          "ref": [
            "college_db.s.student_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 1,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "0.43",
            "eval_cost": "0.17",
            "prefix_cost": "1.85",
            "data_read_per_join": "54"
          },
          "used_columns": [
            "student_id",
            "course_id"
          ],
          "attached_condition": "(`college_db`.`e`.`course_id` is not null)"
        }
      },
      {
        "table": {
          "table_name": "c",
          "access_type": "eq_ref",
          "possible_keys": [
            "PRIMARY"
          ],
          "key": "PRIMARY",
          "used_key_parts": [
            "course_id"
          ],
          "key_length": "4",
          "ref": [
            "college_db.e.course_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 1,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "0.43",
            "eval_cost": "0.17",
            "prefix_cost": "2.45",
            "data_read_per_join": "1K"
          },
          "used_columns": [
            "course_id",
            "course_name"
          ]
        }
      }
    ]
  }
} */

/*
Question 49:

The EXPLAIN output shows a Full Table Scan on the students table.
Evidence:
- access_type = ALL
Reason:
- No index exists on students.enrollment_year.
- MySQL scans all rows before applying the filter condition.
*/

/*
Question 50:

Rows Examined:
- students table: 10 rows
- enrollments table: 1 row
- courses table: 1 row
Estimated Query Cost:
- 2.45
Observation:
The students table examines the highest number of rows because it performs a Full Table Scan.
The enrollments and courses tables use indexes, resulting in fewer rows examined.
*/

-- TASK 2

create index idx_students_enrollment_year
on students(enrollment_year);

create unique index idx_enrollment_student_course
on enrollments(student_id, course_id);

create index idx_course_code
on courses(course_code);

/*
Question 54:

Comparison with Baseline:
Before Index:
- students table access_type = ALL
- Full Table Scan performed
- Rows Examined = 10
After Index:
- students table access_type = ref
- Index idx_students_enrollment_year used
- Rows Examined = 5
Observation:
The query plan changed from Full Table Scan to Index Scan/Index Lookup.
MySQL now uses the idx_students_enrollment_year index, reducing the number of rows examined.
*/

/*
Question 55:

MySQL does not support partial indexes with WHERE conditions.
Partial indexes are supported in PostgreSQL.
Skipped as not applicable in MySQL.
*/
