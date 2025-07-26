'''
1.Add new student
2.show all students
3.update student
4.delete student
5.search student
6.show all student by grade
7

'''

import mysql.connector 

# create connection object

mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db_1248"
)
cursor=mycon.cursor()
def addstudent():
    stud_id=int(input('Enter student id:'))
    stud_name=input('Enter student name :')
    age=int(input('Enter age :'))
    city=input('Enter city :')
    marks=int(input('Enter marks :'))
    stram=input('Enter stream:')

    query="insert into student values(%s,%s,%s,%s,%s,%s)"
    val=(stud_id,stud_name,age,city,marks,stram)
    cursor.execute(query,val)
    mycon.commit()
    print(cursor.rowcount,"Recoerd added..")
def showstudent():
    query="select * from student"
    cursor.execute(query)
    print("stud_id \t stud_name \t Age \t city \t marks \t stream")
    for i in cursor:
        print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {i[5]}")
    mycon.commit()
def updatestudent():
    ch=int(input('Which filed to update \n1.Name\n2.Age\n3.city\n4.marks\n5.stream\nEnter Choice :'))
    if ch==1:
        stud_id=int(input('Enter stud_id ;'))
        stud_name=input('Enter the name :')
        query="update student set stud_name=%s where stud_id=%s "
        val=(stud_name,stud_id)
        cursor.execute(query,val)
        if cursor.rowcount>0:
            print("Recoerd updated..")
        mycon.commit()
    elif ch==2:
        stud_id=int(input('Enter stud_id ;'))
        age=int(input('Enter the age :'))
        query="update student set age=%s where stud_id=%s "
        val=(age,stud_id)
        cursor.execute(query,val)
        if cursor.rowcount>0:
            print("Recoerd updated..")
        mycon.commit()
    elif ch==3:
        stud_id=int(input('Enter stud_id ;'))
        city=input('Enter the city :')
        query="update student set city=%s where stud_id=%s "
        val=(city,stud_id)
        cursor.execute(query,val)
        if cursor.rowcount>0:
            print("Recoerd updated..")
        mycon.commit()
    elif ch==4:
        stud_id=int(input('Enter stud_id ;'))
        marks=int(input('Enter the marks :'))
        query="update student set marks=%s where stud_id=%s "
        val=(marks,stud_id)
        cursor.execute(query,val)
        if cursor.rowcount>0:
            print("Recoerd updated..")
        mycon.commit()
    elif ch==5:
        stud_id=int(input('Enter stud_id ;'))
        stream=input('Enter the name :')
        query="update student set stream=%s where stud_id=%s "
        val=(stream,stud_id)
        cursor.execute(query,val)
        if cursor.rowcount>0:
            print("Recoerd updated..")
        mycon.commit()
def deletestudent():
    stud_id=int(input('Enter stud_id :'))
    query="delete from student where stud_id=%s"
    val=(stud_id,)
    cursor.execute(query,val)
    if cursor.rowcount>0:
        print("Recoerd Deleted..")
    mycon.commit()
def searchstudent():
    stream=input('Enter the stream :')
    query="select * from student where stream=%s"
    val=(stream,)
    cursor.execute(query,val)
    for i in cursor:
        print(i)
    mycon.commit()
def acendingorder():
    ch=int(input('What do want acending order\n1.name\n2.Age\n3.Marks\n Enter your choice:'))
    if ch==1:
        query="select * from student order by stud_name "
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            print(row)
        # cursor.close()
        # mycon.close()
    elif ch==2:
        query="select * from student order by age "
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            print(row)
        # cursor.close()
        # mycon.close()
    elif ch==3:
        query="select * from student order by marks "
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        mycon.close()
def searchname():
    stud_name=input('Enter the letter :')
    query="select * from student where stud_name like %s"
    
    val = (str(stud_name + '%'),)
    # val=(stud_name,)
    cursor.execute(query,val)
    result=cursor.fetchall()
    if result:
        for row in result:
            print(row)

   
ans='Y','y'
while(ans=='Y'or 'y'):

    print("------Welecome to student crud app-----")
    print()
    print("\t\t\t 1.add new student")
    print("\t\t\t 2.show all student")
    print("\t\t\t 3.update student")
    print("\t\t\t 4.delete student")
    print("\t\t\t 5.search student by stram")
    print("\t\t\t 6.show all student in acending order")
    print("\t\t\t 7.Search the student name using lettter")
    print("\t\t\t 8.Exit")
    choice=int(input('Enter Your Choice :'))
    if choice==1:
        addstudent()
    elif choice==2:
        showstudent()
    elif choice==3:
        updatestudent()
    elif choice==4:
        deletestudent()
    elif choice==5:
        searchstudent()
    elif choice==6:
        acendingorder()
    elif choice==7:
        searchname()
    elif choice == 8:
        print('thank you')
        break
    ans=input('Do u want to Continue Y/N: ') 