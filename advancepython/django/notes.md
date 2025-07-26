<!-- Django is high level python framework. it helpt to createe powerfull web application


Django is a high-level, open-source Python web framework that allows developers to build secure, scalable, and maintainable websites quickly and efficiently.


Djnago provided some in built features like;
 1]Authentication
 2]ORM-(pbject Relational Mapping)
 3]DataBase Connectvity
 4]Admin Panel
 5]MVT(Model View Templates)

 <!-- Tuz project structur chukal e 
  -->

by default 11 table are already in the django


# Input from u
text = input("Enter a string or number: ")

# Reverse the input
reversed_text = text[::-1]

# Check if palindrome
if text == reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")



the env activate of using this comand 
D:\kiran acadmy\betch1248\advancepython\django>myenv\Scripts\activate


to  create the project the using this cmd
(myenv) D:\kiran acadmy\betch1248\advancepython\django>django-admin startproject staticfileserving

(myenv) D:\kiran acadmy\betch1248\advancepython\django>cd staticfileserving


the create the app to using this cmd
(myenv) D:\kiran acadmy\betch1248\advancepython\django\staticfileserving>python manage.py startapp app1

(myenv) D:\kiran acadmy\betch1248\advancepython\django\staticfileserving>code .

(myenv) D:\kiran acadmy\betch1248\advancepython\django\staticfileserving>


---------------------------------------------------------------------------------------------------------------------------------------------------------------

static file     
    the extrenal file are include in the django the using the staic file 

-----------------------------------
# Model and superuser
    1]superuser:
        in main project in urls.py already provide the admin panel in the django
        urls.py-
        path('admin\',admin.site.urls)

        the username and password are create this using the command
         cmd: python manage.py createsuperuser

        SQL code crete - python manage.py makemigration
        SQL code Execute - python manage.py migrate 

    2]Model
        the create a class
        models mean class


Interview qusations
1] what are model in Django
2]Define static  files and explain thir uses?
3] what is django_admin and manage.py and explain it's command
4] what is Templating?and how it is used?
5] explain django architecture?
6]What is the difference between project and an app in Django?
7] what is Django.showrtcuts.render function
8] what is the signficance of setting.py file


# ORM (objet Relational maping):
    Convert the python code  file to db language
 * ORM Commands:
    shell Prompt: python manage.py shell

    create the object 
        # Insert the data
        >>> obj=student(studName="Rohit",age=23,stream="BCA",city="Pune",marks)
        >>> obj.save()
        >>> student.objects.create(studName="Sarthak",age=20,stream="MCA",city="Pune",marks=95)  
        

        # Show all data
            data=student.objects.all()
            >>> for i in data:
            ...     print(i.studName,i.age,i.marks)
        # To get the specifc student details
            >>> data=student.objects.get(id=3)
            >>> print(data) 
            student object (3)
            >>> print(data.id,data.studName,data.age)
            3 Durgesh 22
            >>>
        # using the Filter:
            data=student.objects.filter(stream="BCA")
            >>> for i in data:
            ...     print(i.studName)
            ...  


        # greate than 
            data=student.objects.filter(age__gte=22)
            >>> for i in data:       
            ...     print(i.studName,i.age)

        # Two condition :
            >>> data=student.objects.filter(age__gt=22,stream="MCA")
            >>> for i in data:
            ...     print(i.studName,i.stream)


        #  OR ,& condition:
            data=student.objects.filter(Q(studName='Rohit') | Q (marks=80))
            >>> for i in data :
            ...     print(i.studName)


        # Update 
            >>>student.objects.filter(id=1).update(studName="ABC")
        
        # Delete
            >>> student.objects.filter(id=1).delete()
            (1, {'student.student': 1})
            

    # Master Page Creation
        In Django, master pages refer to a base template — a common layout used across multiple pages of a website. Instead of repeating the same HTML structure in every file (like headers, navbars, footers), Django allows you to create a base file and let other pages inherit it.

























