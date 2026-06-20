#TASK 4

import time
import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)
cursor = conn.cursor()
query_count=0
start_time = time.time()
cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()
query_count+=1
for enrollment in enrollments:
    student_id=enrollment[1]
    cursor.execute("SELECT first_name,last_name FROM students WHERE student_id=%s",(student_id,))
    student_info = cursor.fetchone()
    print(f"Student ID:{student_id},"
          f" Student Name: {student_info[0]} {student_info[1]}"
    )
    query_count+=1
print("\nQueries Executed:",query_count)
end_time = time.time()
n_plus_one_time = end_time - start_time
print("Execution Time:", n_plus_one_time)


query_count = 0
cursor = conn.cursor()
start_time = time.time()
cursor.execute(
    """select e.student_id,s.first_name,s.last_name
    from enrollments e join students s 
    on e.student_id = s.student_id
    """)
records = cursor.fetchall()
query_count += 1

for record in records:
    print(
        f"Student ID: {record[0]}, "
        f"Student Name: {record[1]} {record[2]}"
    )
print("\nQueries Executed:", query_count)
end_time = time.time()
join_time = end_time - start_time
print("Execution Time:", join_time)
print("Queries in N+1:", len(enrollments) + 1)
print("Queries in JOIN:", 1)
cursor.close()
conn.close()

""""
Student ID:1, Student Name: Arjun Mehta
Student ID:1, Student Name: Arjun Mehta
Student ID:2, Student Name: Priya Suresh
Student ID:2, Student Name: Priya Suresh
Student ID:3, Student Name: Rohan Verma
Student ID:5, Student Name: Vikram Das
Student ID:5, Student Name: Vikram Das
Student ID:6, Student Name: Kavya Menon
Student ID:8, Student Name: Deepika Rao
Student ID:8, Student Name: Deepika Rao
Student ID:9, Student Name: Meera krishnan
Student ID:9, Student Name: Meera krishnan

Queries Executed: 13
Execution Time: 0.008166074752807617
Student ID: 1, Student Name: Arjun Mehta
Student ID: 1, Student Name: Arjun Mehta
Student ID: 2, Student Name: Priya Suresh
Student ID: 2, Student Name: Priya Suresh
Student ID: 3, Student Name: Rohan Verma
Student ID: 5, Student Name: Vikram Das
Student ID: 5, Student Name: Vikram Das
Student ID: 6, Student Name: Kavya Menon
Student ID: 8, Student Name: Deepika Rao
Student ID: 8, Student Name: Deepika Rao
Student ID: 9, Student Name: Meera krishnan
Student ID: 9, Student Name: Meera krishnan

Queries Executed: 1
Execution Time: 0.0026111602783203125
Queries in N+1: 13
Queries in JOIN: 1
"""

"""
Question 59:

For 10,000 enrollments:

N+1 Approach:
1 query to fetch enrollments
+ 10,000 queries to fetch student details
Total Queries = 10,001

JOIN Approach:
1 query only
Extra Queries Issued by N+1 Approach = 10,000
Observation:
The JOIN approach is significantly more efficient and scalable than the N+1 approach.
"""