# '''
# '''#'''Write a program to create a class Car with attributes brand and price, and a method to display details.
# ''''class car():
#     shroumnm="Rohit Sonawane" # class attributes
#     def __init__(self,brand,price):
#         self.brand=brand #instance attribute
#         self.price=price
#     def display(self):
#         print(f"the car brand is {self.brand} and this car price is {self.price} and this is the showrum name {self.shroumnm}")

# car1=car("BMW", 100000000)

# car1.display()'''

# '''
# Write a Python program to create a class Student with:

# Instance attributes: name, roll_no

# A method show() to display student details
# Create two student objects and display their data.


# class student():
#     def __init__(self,rno,nm):
#         self.rollNO=rno
#         self.name=nm

#     def show(self):
#         print(f"the student rollno={self.rollNO} and name is = {self.name}")

# stud1=student(101,"Rohit")
# stud2=student("102",'vijay')
# stud1.show()
# stud2.show()
# '''

# '''
# Create a class Employee with:

# Instance attributes: name, salary

# A class attribute: company_name = "Infosys"
# Create 2 employee objects and print their details along with the company name.



# class employee():
#     company_name="TCS"
#     def __init__(self ,nm,sal):
#       self.name=nm
#       self.salary=sal
#       print(f"the employee name is = {self.name} and her salary is = {self.salary} and this company name is = {self.company_name}")

# employee1=employee("rohit",500000)
# employee2=employee("vijay",500000)
# '''
# '''
# Create a class Book that initializes the following using constructor:

# title, author, price
# Include a method details() to print book information.
# Create an object and show details.
# '''
# # class book():
# #     def __init__(self,tile,author,price):
# #         self.title=tile
# #         self.author=author
# #         self.price=price

# #     def show(self):
# #         print(f"the book name is = {self.title} the author name of book is = {self.author} and the price of book is = {self.price}")

# # book1=book('abc','vijay',700)
# # book2=book('xyz','santosh',800)

# # book1.show()
# # book2.show()
# '''
# Create a class Vehicle with:

# Class attribute: wheels = 4

# Instance attributes: brand, model
# Method info() should display brand, model, and wheels.
# '''
# # class vehicle ():
# #     wheels=4
# #     def __init__(self,brand,model):
# #         self.brand=brand
# #         self.model=model

# #     def info(self):
# #         print(f"the brand is = {self.brand} the model is = {self.model}and the type is = {self.wheels}")

# # v1=vehicle("BMW", "1st")
# # v1.info()
# # '''


# #encapsulation
# '''Q. Write a Python class called BankAccount that demonstrates encapsulation. Your program should:
# Create private variables for account_holder and balance.

# Create a method to deposit money into the account (only if amount > 0).

# Create a method to withdraw money (only if balance is sufficient).

# Use getter and setter methods to get the account holder name and update it (name should only contain alphabets).

# Use the @property decorator for accessing and setting the balance.'''

# class bank:
#     def __init__(self,acch,bal):
#         self.__account_holder=acch
#         self.__balance=bal

#     @property
#     def get_deposite(self):
#         return self.__balance
    
#     @get_deposite.setter
#     def set_deposite(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             return f'your bank account is deposited : {amount} '
#         else:
#             return 'invalid amount'
#     @property
#     def get_withdraw(self):
#         return self.__balance

#     @get_withdraw.setter
#     def set_withdraw(self,amount):
#         if amount<self.__balance:
#             self.__balance-=amount
#             return f' Your withdraw is seccfulyy of the {amount}'
#         else:
#             return 'insufficant founds'
    
#     @property 
#     def get_name(self):
#         return self.__account_holder
    
#     @get_name.setter
#     def set_name(self,name):
#         if isinstance(name,str)and name.isalpha:
#             self.__account_holder=name

# b1=bank('rohit',20000)
# # print("name",b1.__account_holder)
# # print('balance',b1.__balance)
# b1.set_deposite=100
# print(b1.get_deposite)
# b1.set_withdraw =4000
# print(b1.get_withdraw)
# # print(b1.withdraw(200000))
# # print(b1.get_name)
# # b1.set_name='rahul'
# # print(b1.get_name)

# f=open('data.txt','r')
# count=0
# for i in f:
#     count+=1
# f.close()
# print(count)

# f=open('data.txt','r')
# for i in f:
#     print(i.title(),end='')
'''

Check if a Number is Even or Odd

Description: Use modulus operator % and if-else to check number properties.

'''
# num=int(input('Enter a number :'))
# if num %2==0:
#     print('This is the even number ')
# else:
#     print('This is the odd number ')

'''
Print Numbers from 1 to 10 using a Loop

Description: Helps understand how for or while loops work.

'''
# for i in range(1,11):
#     print(i)

# i=1
# while i<11:
#     print(i)
#     i+=1
'''
Find the Sum of First N Natural Numbers

Description: Learn how to use loops with a running total.

'''

# for num in range(1,11):
#     total=sum(range(1,num+1))
#     print(total)

'''Check if a Number is Positive, Negative, or Zero

Description: Practice nested if-elif-else conditions.'''

# num=int(input('Enter a number :'))
# if num>0:
#     print('the number is postive')
# else:
#     print('the number is negative')

'''Find the Largest of Two Numbers

Description: Comparison using simple if-else logic.
'''

# num1=int(input('Enter the first number :'))
# num2=int(input('Enter a second number :'))
# if num1>num2:
#     print(f' the {num1} is largest of {num2}')
# else:
#     print(f'the {num2}is greater than {num1}')

'''Swap Two Numbers Without Using a Third Variable

Description: Logical use of arithmetic operations.
'''
# a=int(input('Enter the first number :'))
# b=int(input('Enter second number :'))
# a=a+b
# b=a-b
# a=a-b
# print('after swaping')
# print('the a value is ',a)
# print('the b value is ',b)

'''Check if a Year is a Leap Year

Description: Logical operators with multiple conditions.
'''

'''Print the Multiplication Table of a Number

Description: Practice nested loops and formatting output.'''

# for i in range(2,21,2):
#     print(i)

# rows=10
# cols=10
# for i in range(1,rows +            1 ):
#     for j in range(1,cols + 1):
#         print(f'{i*j}   ',end='  ')
#     print()

'''Count the Number of Digits in a Number

Description: Learn to break down numbers using division and modulus.
'''

'''Reverse a Number

Description: Loop and logic to build reversed number from digits.

'''

# num=612345
# for i in str(num[::-1]):
#     print(i)

'''Count Vowels in a String

Description: Loop through strings and use conditional checking.
'''

# name=str(input('Enter a name :'))
# vowels='aeiouAEIOU'
# count=0
# for check in name:
#     if check in vowels:
#         count+=1
# print(count)

'''sum of Elements in a List

Description: Use of for loop or built-in sum() to understand iterables.
# '''
# num=[12,12]
# result=0
# for number in num:
#     result+=number
#     print(result)

'''
Find the Maximum Number in a List

Description: Manual traversal using for loop and logic.

'''
number=[11,23,23,12,56]
max_num=number[0]
for num in number:
    if num>max_num:
        max_num=num
print(max_num)