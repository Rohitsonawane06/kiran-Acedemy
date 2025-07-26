# # '''
# # open method :
# # this the method to file open
# # syntax:
# # open=>open(filename,mode)


# # '''
# # #open method example:
# # f=open('data.txt','r')
# # for i in f:
# #     print(i)


# # #attributes
# # '''
# # closed : to check file open or cloase and return boolen 
# # Name : to check file name
# # mode : to check mode which file open
# # '''
# # print(f.closed)
# # print(f.name)
# # print(f.mode)


# # '''
# # close method:
# # this the method are to help the file close
# # syntax:
# # f.close()

# # '''
# # #close method example:
# # print('before cloase method',f.closed)
# # f.close()
# # print('after cloase method',f.closed)

# # #opration
# # '''
# # read()=>read the file
# # readline()=>read a sing line
# # readlines()=>all the data read but reading the list form
# # '''

# # #1]reading
# # #1]read()=>read all data the using the r mode the by default is -1  
# # f=open('data.txt','r')
# # print(f)

# # #2]readline()=> to read thr single line the end using the \n delete
# # f=open('data.txt','r')
# # data1=f.readline()
# # print(data1,end='')
# # data2=f.readline()
# # print(data2,end='')


# # method of readline()
# # 1] tell=> this the tell the retrun the position
# # f=open('data.txt','r')
# # print(f.tell())
# # # 2]seek()=>set the string position 

# # f=open('data.txt','r')
# # f.seek(15)
# # print()

# #3]readlines()=> this the method are read all data but   in the list form
# # f=open('data.txt','r')
# # data=f.readlines()#['hellow student\n', 'welcome to kiran academy\n', 'karve nagar\n']
# # print(data)


# # write method
# '''
# write the data to using the this mode=> 'W','a','x'

# '''
# #1]Mode=W
# '''
# this the method the file are present the override the file but the file not present to create the file
# '''
# '''
# write method
# usig the w mode to override all data 
#  the file are not present to create the file
#  ''' 
# # f=open('data1.txt','w')
# # f.write("Hellow student ")# write string s to stream
# # f.close()

# '''writeline method
# to the mutiple line write
# it is the iterable to present the file to override and the file are not present to creare and the fill the data
# '''
# # f=open('coursces.txt','w')
# # f.writelines(['python \n','java \n','c'])
# # f.close()

# '''

# Mode=a
# a=append
# the mode are add the last are append the same file 
# the file are present add the last of the file
# the file are not present to create and the fill the data
# '''
# # f=open('coursces.txt','a')
# # f.write('\nhtml')
# # f.close()

# '''
# Mode=x
# the  file are the present in the system the not write the file to send exception 
# the  file are not present to create and the fill the data
# '''
# # f=open('coursces.txt','x') #FileExistsError: [Errno 17] File exists: 'coursces.txt'
# # f.write('mysql')
# # f.close()


# #readable => the method are check the read or not
# f=open('coursces.txt','r')
# print(f.readable())#True

# print(f.writable())#False
# #writeable=> the method are check the write or not
# f=open('coursces.txt','w')
# print(f.writable())#True
# print(f.readable())#False

# #mode r+ =>this mode are work are both opration are working  (readable= to read the file and writeable=write the file)
# f=open('coursces.txt','r+')
# print(f.readable())#True

# print(f.writable())#True

# #mode w+=>his mode are work are both opration are working  (readable= to read the file and writeable=write the file)
# # f=open('coursces.txt','w+')
# # print(f.readable())#true
# # print(f.writable())#true


# f=open('tkacdemy.txt','r')
# print('Available courses are:')
# sr=1
# for i in f:
#    print(f'{sr}.{i}')
#    sr+=1

# f=open('result.txt','r')
# for student in f:
#     list_data=student.split()
#     obt_mark=0
#     for mark in list_data[1:]:
#         obt_mark+=int(mark)
#     perc=obt_mark/len(list_data[1:])
#     f2=open('percentage.txt','a')
#     f2.write(f'{list_data[0]} {perc}\n')

# f=open('oneplus.txt','r')
# for model in f:
#     list_data=model.split()
#     real_price=0
#     for price in list_data[1:]:
#         discount=int(price)/10
#         d_price=int(price)-discount
#     f2=open('discount.txt','a')
#     f2.write(f'{list_data[0]} {d_price}\n')
  

# f=open('oneplus.txt','r')
# for model in f:   
#         list_data=model.split()
#         price=int(list_data[1])-(int(list_data[1])/10)
#         print(price)
#         f2=open('discount.txt','a')
#         f2.write(f'{list_data[0]} {price}\n')
  
   
    
'''
Create a file numbers.txt and write numbers 1 to 10 (each on a new line) using a loop.

Read numbers.txt and print only even numbers.

    '''
# f=open('number.txt','w')
# for i in range(1,11):
#     f.write (str(i)+'\n')

# f=open('even.txt','r')
# for number in f:
#         num=int(number.strip())
#         if num %2==0:
#                 print(num)
# f2=open('even.txt','a')
# f2.write(f'{num}')
        
