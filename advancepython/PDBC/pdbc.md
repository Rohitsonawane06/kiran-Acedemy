import the module mysql-connector-python
pip install mysql-connector-python

1.import mysql-connector module
2.create connection ovject
    nycon=mysql.connector.connect(
        username="root",
        password="root",
        hot="localhost",
        database="db_1248" if the database aleready create use 
    )
3.create cursor(is a class)--cussor=mycon.cursor()
4.write Query--query="select * from studeng"
5.Excute Query using cursor.execute(query)