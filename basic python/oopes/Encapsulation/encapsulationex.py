'''
Encapsulation
Encapsulation
    wraping of the data within the single unit in a class is called is encapsulation 

>Public variable
    we can access public outside of the class and we can modifly it is called a public variable
>private variable

> gettr and setter method

'''

'''

Public variable
    we can access public outside of the class and we can modifly it is called a public variable
'''
# class Counter:
#     def __init__(self):
#         self.count=0
#     def inc(self):
#         self.count+=1
#     def dec(self):
#         self.count-=1
#     def check(self):
#         print(self.count)

# c=Counter()
# c.check()
# c.inc()
# c.inc()
# c.inc()
# c.inc()
# c.inc()
# c.check()
# c.dec()
# c.check()
# c.count=1000
# c.check()

'''
private variable
    the duble underscore(__)using create the private  varibale
    we can access the outside of the class only for access the method any method in only class we cant modefiy the private variable

'''
class Counter:
    def __init__(self):
        self.__count=0
    def inc(self):
        self.__count+=1
    def dec(self):
        self.__count-=1
    def check(self):
        print(self.__count)

c=Counter()
c.check()
c.inc()
c.inc()
c.inc()
c.inc()
c.inc()
c.check()
c.dec()
c.check()
''''

 1]getter method 
    private variable value the access using getter method
 2]setter method
    send the value of the private variable using the setter method

'''

class student:
    def __init__(self,nm,age):
        self.__name=nm
        self.__age=age
    #getter method
    def get_name(self):
        return self.__name , self.__age
    # setter method
    def set_age(self,aage):
        self.__age=aage
    # def set_name(self,nname):
    #     if isinstance(nname,str)and nname.isalpha():
    
    #          self.__name=nname



s1=student('rohit',21)
s2=student('vijay',22)
print(s1.get_name())
# s1.set_name('rohitpatil')
s1.set_age(23)
print(s1.get_name())


'''
@property
using property decoarate the using a work a like attribute for the getter method

the setter name using the decorate the using the getname method and . setter the
the worke is the attribute 

'''
class student:
    def __init__(self,nm,age):
        self.__name=nm
        # self.__age=age
    #getter method

    @property
    def get_name(self):
        return self.__name 
    
    @get_name.setter
    def set_name(self,nname):
        if isinstance(nname,str)and nname.isalpha():
             self.__name=nname



s1=student('rohit',21)
s2=student('vijay',22)
print(s1.get_name)
s1.set_name='rahul'
# s1.set_age(23)
print(s1.get_name)