'''
using the method name to overload the oprator

'''
# class book:
#     def __init__(self,nm,pg):
#         self.name=nm
#         self.pages=pg
#     def __add__(self,other):
#         return self.name + other.name ,self.pages+other.pages
     



# b1=book("python ",100)
# b2=book("java",200)
# print(b1+b2)




# class book:
#     def __init__(self,nm,pg):
#         self.name=nm
#         self.pages=pg
#     def __add__(self,other):
#         total= self.pages+other.pages
#         return book ('x',total)
#     def __str__(self):
#         return f'toal number of pages is :{self.pages}'



# b1=book("python ",100)
# b2=book("java",200)
# b3=book("C",300)
# print(b1+b2+b3)

class Hotel :
    def __init__(self,nm,rate):
        self.name=nm
        self.rate=rate
    def __gt__(self,other):
       if self.rate>other.rate:
           return f'the {self.name} hotel rate are greater than {other.name}'
       else:
           return f'the {other.name} hotel rate are greater than {self.name}'



h1=Hotel('raj',10000)
h2=Hotel('taj',20000)
print(h1>h2)