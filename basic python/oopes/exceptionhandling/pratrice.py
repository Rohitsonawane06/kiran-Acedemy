# def division(n1,n2):
#     try:
#         div=n1/n2
#     except:
#         n2=eval(input('we can divide by the zero please enter again n2 :'))
#         result= division(n1,n2)
#         return result
#     else:
#         return div
# print(division(10,0))

# def copy_data(meanfile,ogfile):
#     try:
#         f1=open(meanfile,'r')
#     except FileNotFoundError:
#         meanfile=input('Enter correct file name :')
#         copy_data(meanfile,ogfile)
#     else:
#         data=f1.read()
#         f2=open(ogfile,'w')
#         f2.write(data)
# copy_data('clear.txt','myfile1248.txt')

# def count_line(file):
#     try:
#          f1=open(file,'r')
#     except:
         
#         meanfile=input('Enter correct file name :')
#         copy_data(meanfile,ogfile)
#     else:
#         list_line=f1.readlines()
#         print(len(list_line))

# count_line('data.txt')

# def check_word(file1):
#     try:
#         f1=open(file1,'r')
#         lines=f1.readlines()

#     except:
#         file1=input('Enter the correct file name :')
#         return check_word(file1)
#     else:
#         count=0
#         for worrd in lines:
#             result=worrd.split()
#             count=count+len(result)
#         return count
# print(check_word('data2.txt'))

# #-----------------------------------------------------------------------------
# # create a function to count of character in the file without exception handling but using function
# def char_count(file):
#     try:
#         f1=open(file,'r')
#         data=f1.read()
#     except:
#         file=input('Enter the correct name of file :')
#         return char_count(file)
#     else:
#         count=0
#         for char in data:
#             if char != ' ':
#                 count+=1
#         return count
    
# print(char_count('data3.txt'))

#---------------------------------------------------------------------------------------
# def value_error():
#     try:
#         n1=int('rahul')
#     except ValueError as e:
#         print(e)
#     else:
#         return n1
# print(value_error())



# def synatx_error():
#     try:
#         n1 10
#         n2=20

#     except SyntaxError as e:
#         print(e)
#     else:
#         result=n1+n2
#         return result
# print(synatx_error())


# def value_error():
#     try:
#         n1=int(input('Enetr the n1 value:'))
#         n2=int(input('Enter the n2 value :'))
#         result=n1+n2
#         return result
#     except ValueError as e:
#         print(e)
# print(value_error())

# def indentation_error():
#     try:
#         my_list=[10,20,30,40]
#          for i in my_list:
#          print(i)
#     except IndentationError as e:
#         print(e)

# print(indentation_error())

def index_error():
    try:
        my=[10,20,30]
        print(my[4])
    except IndexError as e:
        print(e)
print(index_error())