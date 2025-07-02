# pip install db-sqlite3
# pip install sqlite3
import sqlite3

#Connectt to SQlite
#Our database name: Naresh_it_student
connection=sqlite3.connect("Student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()
cursor.execute("DROP TABLE IF EXISTS Student_details")

#create the table
#Our table name student
#Columns names are: name, course
table_info="""
Create table Student_details(student_name varchar(30),
                    student_Id int,
                    student_course varchar(30),
                    course_fee float);
"""
cursor.execute(table_info)

#Insert the records

cursor.execute('''Insert Into Student_details values('Ramu',101,'Data Science',50000)''')
cursor.execute('''Insert Into Student_details values('Naresh',102,'Data Analyst',20000)''')
cursor.execute('''Insert Into Student_details values('Phanidra',103,'Data Science',68000)''')
cursor.execute('''Insert Into Student_details values('Naga babu',104,'Java',50000)''')
cursor.execute('''Insert Into Student_details values('Ajay',105,'Data science',35000)''')
cursor.execute('''Insert Into Student_details values('Pawan',106,'Devops',60000)''')

#Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from Student_details''')
for row in data:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()