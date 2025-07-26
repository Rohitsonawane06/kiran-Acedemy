import mysql.connector
myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="capgemini"
)
cursor=myconn.cursor()
# cursor.execute("show tables")
# for x in cursor:
#     print(x)

#create table
#query="create table person(pid int primary key,pname varchar(20),city varchar(20),age int)"

#insert recoerd
#query="insert into person values(%s,%s,%s,%s)"
# val=[
#     (1,'Rohit','pune',21),
#     (2,'Vijay','Nashik',22),
#     (3,'Santosh','Pune',21),
#     (4,'Durgesh','Nashik',20)

# ]
# cursor.executemany(query,val)
# myconn.commit()
# print(cursor.rowcount,"Recoerd inserted..")


#show Recoerd
# query="select*from person"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()
# print(cursor)

#5. Display only names of students from Pune.
# query="select pname from person where city='pune'"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()
# print(cursor)

# 6. Update age of 'Durgesh' to 21.
# query="update person set age=21 where pname='Durgesh'"
# cursor.execute(query)
# myconn.commit()
# print(cursor.rowcount,'recoerd updated')

# 7. Delete the record of 'Vijay'.
# query="delete from person where pname='vijay'"
# cursor.execute(query)
# myconn.commit()
# print(cursor.rowcount,"Recoerd updated..")

# 9. Sort the students by age in descending order.
# query="select * from person order by age desc"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()
# print(cursor,"Sorted data")

#10. Find students with age greater than 20.
# query="select *from person where age>20"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()


# 11. Find all students who live in Nashik.
# query="select * from person where city='nashik'"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()

# 12. Display only name and age of students.
# query="select pname,age from person"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()

#  13. Add a new column email to the table.
# query = "ALTER TABLE person ADD email VARCHAR(100)"
# cursor.execute(query)
# print("Column 'email' added successfully.")
# myconn.commit()
# print(cursor.rowcount,"Recoerd addedd")
# cursor.close()
# myconn.close()

# 14. Update the email of Rohit to rohit@gmail.com.
# query="updated person set email='rohit@gmail.com' where pname='Rohit'"
# cursor.execute(query)
# myconn.commit()
# print(cursor.rowcount,"Recoerd updated..")

# query = "UPDATE person SET email='rohit@gmail.com' WHERE pname='Rohit'"
# cursor.execute(query)
# myconn.commit()
# print(cursor.rowcount, "Record updated..")

#15. Find the average age of all students.
# query="select avg(age) from person"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()
# print(cursor.rowcount,"avg age is")

# 16. Count total number of students.
# query="select count(*) from person"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()

#17. Insert a new student record:
# query="alter table person values(5,'Amit','pune',21,'amit@gmail.com')"
# cursor.execute(query)
# print("Record addedd..")
# myconn.commit()
# print(cursor.rowcount,"recoerd add")
# cursor.close()
# myconn.close()

# query = "INSERT INTO students (id, name, city, age, email) VALUES (%s, %s, %s, %s, %s)"
# values = (5, 'Amit', 'Pune', 21, 'amit@gmail.com')

#19. Find the youngest student (minimum age).
# query="select *from person order by  age limit 1"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()
# print(cursor.rowcount,"recoerd display")

# 20. Drop the email column.
# query="alter table person drop column email"
# cursor.execute(query)
# for x in cursor:
#     print(x)
# myconn.commit()

# 18. Delete all students from Pune.
query="delete from person where city='pune'"
cursor.execute(query)
# for x in cursor:
#     print(x)
myconn.commit()
print(cursor.rowcount,"Recoerd deleted..")