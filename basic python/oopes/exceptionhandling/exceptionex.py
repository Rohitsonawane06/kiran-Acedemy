'''Exception handling in Python is a mechanism to manage runtime errors, preventing abrupt program termination. It involves using try, except, else, and finally blocks to handle exceptions gracefully. The try block encloses code that might raise an exception. If an exception occurs, the except block catches and handles it. The else block executes if no exceptions occur in the try block, and the finally block ensures code execution regardless of exceptions. This structure enables programs to respond to errors, maintain stability, and provide a more user-friendly experience. '''


'''
Exception Handling
>try,except,else,finally
custom exception class
raise condition




try:    
    risky code..
except:
    to handle the error
'''
# n1=int(input('Enter the num1 value :'))
# n2=int(input('Enter the num2 value :'))
# # div=n1/n2
# # print(div)
# # print('coding.........')

# #using try and except
# n1=int(input('Enter the num1 value :'))
# n2=int(input('Enter the num2 value :'))
# try:
#     div=n1/n2
#     print(div)
# except:
#     print('We can the any number are divided by zero')
# print('coding.........')

'''
1] try=?risky code
2]except=>code to handle
3] else=>
4]finally=>

1]if the exception are come to excute the except block and finally print
2]if the not except in the code to excute the else block and finally print
'''

# n1=int(input('Enter the num1 value :'))
# n2=int(input('Enter the num2 value :'))
# sum=n1-n2
# sub=n1+n2
# try:
#     div=n1/n2
   
# except:
#     print('We can the any number are divided by zero')
# else:
#     print(div)
# finally:
#         print(sum)
#         print(sub)
#print('coding.........')



# n1=int(input('Enter the num1 value :'))
# n2=int(input('Enter the num2 value :'))
# sum=n1-n2
# sub=n1+n2
# try:
#     div=n1/n2
   
# except ZeroDivisionError as e:
#     print(e)
# except NameError:
#      print('check the name')
     



'''

raise condition
the forecfully error in the code with
'''
# age=int(input('Enter the age :'))
# if age<0:
#     raise ValueError ('check the value')
# print(f'your age is {age}')


'''
custome exception class
the create the own exception in the code are using the class exception
'''
class FiveDivisionError(Exception):
    pass

n1=10
n2=5
if n2==5:
    raise FiveDivisionError('division by zero')#FiveDivisionError: division by zero
print(n1/n2)
