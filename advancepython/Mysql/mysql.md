MYSQL=>it is open source relational database management system to manage data.it is useful for to perfrom different types of 
database related oprataions like fetch data,update data,delete data and many more..



Database==>schema.it is a container to store some tables

Table==> collection of data

Data==> roows and columns info


Data types in sql
1]int
2]varchar
3]float
4]Date
5]Blob,Clob

database create
create database db_name;

select databse
use db_name;

create table
create  table student();

insert table
insert int0 tablename valueS();

mysql> show tables;
+-------------------+
| Tables_in_db_1248 |
+-------------------+
| student           |
+-------------------+
1 row in set (0.02 sec)

mysql> desc student;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| stud_id   | int         | YES  |     | NULL    |       |
| stud_name | varchar(20) | YES  |     | NULL    |       |
| age       | int         | YES  |     | NULL    |       |
| city      | varchar(20) | YES  |     | NULL    |       |
| marks     | int         | YES  |     | NULL    |       |
| stream    | varchar(20) | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
6 rows in set (0.02 sec)

mysql> insert into student values(101,"Rohit",23,"Pune",78,"BCA");
Query OK, 1 row affected (0.03 sec)

mysql> select*from student;
+---------+-----------+------+------+-------+--------+
| stud_id | stud_name | age  | city | marks | stream |
+---------+-----------+------+------+-------+--------+
|     101 | Rohit     |   23 | Pune |    78 | BCA    |
+---------+-----------+------+------+-------+--------+
1 row in set (0.00 sec)

mysql> insert into student values(102,"Harshal",22,"Nashik",68,"BCA");
Query OK, 1 row affected (0.01 sec)

mysql> insert into student values(103,"Durgesh",21,"Mumbai",88,"BBA");
Query OK, 1 row affected (0.01 sec)

mysql> insert into student values(103,"Durgesh",21,"Mumbai",88,"BBA"),(104,"Vijay",23,"Pune",78,"BCA");
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select*from student;
+---------+-----------+------+--------+-------+--------+
| stud_id | stud_name | age  | city   | marks | stream |
+---------+-----------+------+--------+-------+--------+
|     101 | Rohit     |   23 | Pune   |    78 | BCA    |
|     102 | Harshal   |   22 | Nashik |    68 | BCA    |
|     103 | Durgesh   |   21 | Mumbai |    88 | BBA    |
|     103 | Durgesh   |   21 | Mumbai |    88 | BBA    |
|     104 | Vijay     |   23 | Pune   |    78 | BCA    |
+---------+-----------+------+--------+-------+--------+
5 rows in set (0.00 sec)

mysql> insert into student values(105,"tejas",23,"Nashik",68,"BBA"),(106,"Sarthak",20,"Mumbai",88,"BBA"),(107,"Hemant",25,"Pune",67,"BCA"),(108,"Santosh",22,"Nashik",78,"BCA");

mysql> select*from student;
+---------+-----------+------+--------+-------+--------+
| stud_id | stud_name | age  | city   | marks | stream |
+---------+-----------+------+--------+-------+--------+
|     101 | Rohit     |   23 | Pune   |    78 | BCA    |
|     102 | Harshal   |   22 | Nashik |    68 | BCA    |
|     103 | Durgesh   |   21 | Mumbai |    88 | BBA    |
|     103 | Durgesh   |   21 | Mumbai |    88 | BBA    |
|     104 | Vijay     |   23 | Pune   |    78 | BCA    |
|     105 | tejas     |   23 | Nashik |    68 | BBA    |
|     106 | Sarthak   |   20 | Mumbai |    88 | BBA    |
|     107 | Hemant    |   25 | Pune   |    67 | BCA    |
|     108 | Santosh   |   22 | Nashik |    78 | BCA    |
+---------+-----------+------+--------+-------+--------+
9 rows in set (0.00 sec)

mysql> select stud_name,age,stream from student;
+-----------+------+--------+
| stud_name | age  | stream |
+-----------+------+--------+
| Rohit     |   23 | BCA    |
| Harshal   |   22 | BCA    |
| Durgesh   |   21 | BBA    |
| Durgesh   |   21 | BBA    |
| Vijay     |   23 | BCA    |
| tejas     |   23 | BBA    |
| Sarthak   |   20 | BBA    |
| Hemant    |   25 | BCA    |
| Santosh   |   22 | BCA    |
+-----------+------+--------+
9 rows in se

using where
select stud_name,age from student where stream="BCA";
+-----------+------+
| stud_name | age  |
+-----------+------+
| Rohit     |   23 |
| Harshal   |   22 |
| Vijay     |   23 |
| Hemant    |   25 |
| Santosh   |   22 |


check the grater than
 select * from student where age>20;

check range 
mysql> select*from student where marks >60 and marks<80;

using between 
mysql> select*from student where marks between 60 and 70;

using and 

mysql> select*from student where marks between 60 and 70;
+---------+-----------+------+--------+-------+--------+
| stud_id | stud_name | age  | city   | marks | stream |
+---------+-----------+------+--------+-------+--------+
|     102 | Harshal   |   22 | Nashik |    68 | BCA    |
|     105 | tejas     |   23 | Nashik |    68 | BBA    |
|     107 | Hemant    |   25 | Pune   |    67 | BCA    |
+---------+-----------+------+--------+-------+--------+

using or oprator
mysql> select*from student where city="Nahik" or age>=23;

using in oprator
mysql> select *from student where city in("Nashik","Pune","Mumbai");

using like oprator
mysql> select*from student where stud_name like 'R%';

using(__)oprator
mysql> select*from student where stud_name like '__r%';

access the last char
mysql> select * from student where stud_name like '%h';


not oprator
mysql> select * from student where city not like "Nashik";


inteview qusations
1]what is mysql
2]what is database and hot to create database write appropriate command
3]explain data types in mysql
4] what is projection in mysql and how to perfrom projection
5]write insert query for adding some speficic columns information
6]explain following oprator
    a]andf
    b]in
    c]or
    d]like
    e] between



update :
mysql> update student set city="Nashik",marks=99 where stud_name="Rohit";
increment==>update student set marks=marks+10 where city="Nashik";

Delete:
mysql> delete from student where stud_name="Harshal";

as=> the column name are chnage using this keyword

mysql> select stud_name as "name" from student;

Alter
1]add=> the columns add
    mysql> alter table student add email varchar(30);

2]modify=> column name are chnage a range are modidy


3]drop=> the delete the table
    mysql> alter table student drop column email;

aggregate method
1]avg
2]max
3]min
4]count
5]sum

constraint
    apply some conditions while createing table or schema

    types of constraint
    a]Not Null 
        should not enter null value
    b] primary key
        uniquikly identified recoerd(should be not repeated the value as well as Null)
    c]unique
        uniquikly identified recoerd 
    d] check
        apply some specific conditions 
    e] foregin(reference )key
        joins two tables(Set the relationshil between two tables)
    f]Default
        set default value for columns
    7]AUTO_INCREMENT
        automatically increase the value for this colomn\

Group By
    The GROUP BY clause in MySQL groups rows with the same values in one or more columns,  allowing you to perform aggregate calculations (like SUM, AVG, COUNT, MAX, MIN) on each group. It's used in a SELECT statement after the WHERE clause and before the ORDER BY clause, if used.

SQL JOIN
    joins means to combine something'
    A joins clause is used to combine data from two or more tables,based on a related column between them

    Types of joins
    1] left joins
        Returns all rows from the left table, and matching rows from the right table. If no match, NULLs from right table.
            syntax:
                SELECT columns
                    FROM table1
                    LEFT JOIN table2
                    ON table1.common_column = table2.common_column;

    2]Right joins
        Returns all rows from the right table, and matching rows from the left table. If no match, NULLs from left table.
        syntax:
            SELECT columns
                FROM table1
                RIGHT JOIN table2
                ON table1.common_column = table2.common_column;

    3] inner joins
        Returns only matching rows from both tables.
        syntax:
            SELECT columns
                FROM table1
                INNER JOIN table2
                ON table1.common_column = table2.common_column;


    4] full other joins
        Combines results of LEFT and RIGHT JOIN. All rows from both tables; unmatched rows will have NULLs.
        syntax:
            SELECT columns
            FROM table1
            LEFT JOIN table2 ON table1.col = table2.col
            UNION
            SELECT columns
            FROM table1
            RIGHT JOIN table2 ON table1.col = table2.col;

