import mysql.connector 

# create connection object

mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db_1248"
)


# if mycon.is_connected:
#     print("Connection Create Sucessfulyy..")
cursor=mycon.cursor()
# cursor.execute("show tables")
# for x in cursor:
#     print(x)

#create new table
#query="create table person(pid int primary key,pname varchar(20),city varchar(20))"
#query="insert into person value(103,'pqr','mumbai')"
#query="update person set city='nashik' where pid=102"
# mycon.commit()
# print(cursor.rowcount,"recoerd updated")

# #insert recoerd dinamically
# pid=int(input('Enter Pid: '))
# pname=input('Enter name :')
# city=input('Enter city : ')
# #query="insert into person values(%s,%s,%s)"
# query = f"INSERT INTO person VALUES({pid}, '{pname}', '{city}')"
# #val=(pid,pname,city)
# cursor.execute(query)
# mycon.commit()
# print(cursor.rowcount,"recoerd added...")


# query="select* from person"
# cursor.execute(query)
# data=cursor.fetchall()
# for i in data:
#     print(i)

# query="insert into person values(%s,%s,%s)"
# val=[
#     (107,"santosh","nashik"),
#     (108,"vijay","nagput"),
#     (109,"durgesg","kathakatal")
    
# ]
# cursor.executemany(query,val)
# mycon.commit()
# print(cursor.rowcount,"recprd are added")


#update record

# query="update person set pname='blake',city='nagpur' where pid=102"
# cursor.execute(query)

# if cursor.rowcount>0:
#     print("Recoerd updated successfully")
# mycon.commit()

# pid=int(input('Enter pid:'))
# pname=input('Enter Person name :')
city=input('Enter city :')
# query="update person set pname=%s,city=%s where pid=%s"
# val=(pname,city,pid)
# cursor.execute(query,val)
# if cursor.rowcount>0:
#     print('Recoerd updated..')
# mycon.commit()

query="delete from person where city=%s"
val=(city,)
cursor.execute(query,val)
if cursor.rowcount>0:
    print("Recoerd deleted")
mycon.commit()