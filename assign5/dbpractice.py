# 2)  Practice DATABASE  
# -Create Database
# -Create 2-3 tables
# -Insert some records
# -Perform diffrent select operations
# -Update some data
# -Delete some data


import sqlite3

with sqlite3.connect("/mnt/c/Users/rajni/internshipwin/student.db") as conn:

    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS student
                   (id INT Primary Key,name VARCHAR(30))
                   """)

    print("Student table created successfully")

    cursor.execute("""insert into student values (101,'Lakshya'),
                   (102,'Tanvi')""")
    
    print("Student Data inserted")

    cursor.execute("""Create table If Not Exists courses
                   (cid int Primary Key, cname varchar(30),studentsenrolled int)
                   """)
    print("Course table created ")

    cursor.execute("""Insert into courses values(2001,"DBMS",360),
                   (2002,"OS",240)""")

    print("Course data inserted")

    cursor.execute("""Create table If Not Exists Enrollment
                   (cid int, sid int, Foreign Key(cid) references courses(cid),Foreign Key(sid) references student(id)) 
                   """)
    print("Enrollment table created")

    cursor.execute("""
    Insert into Enrollment values (101,2001),
                   (102,2002)
                   """)
    print("Enrollment data inserted")
    cursor.execute("Drop table student2")
    print("Student data:")
    cursor.execute("Select * from student") 
    print(cursor.fetchall())
    print("Course data:")
    cursor.execute("Select * from courses")
    print(cursor.fetchall())
    print("Enrollment data:")
    cursor.execute("""Select * from Enrollment
                   """)
    print(cursor.fetchall())
    cursor.execute("Update Enrollment set cid=2001 where cid=101 ")
    cursor.execute("Update Enrollment set sid=101 where sid=2001 ")
    cursor.execute("Update Enrollment set cid=2002 where cid=102 ")
    cursor.execute("Update Enrollment set sid=102 where sid=2002 ")
    print("Data updated")
    cursor.execute("""Select * from Enrollment
                   """)
    print(cursor.fetchall())

    cursor.execute("Delete from Enrollment where sid=102")
    print("Data deleted")
    cursor.execute("""Select * from Enrollment
                   """)
    print(cursor.fetchall())
