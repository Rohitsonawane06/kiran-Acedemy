def check_word(file1):
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