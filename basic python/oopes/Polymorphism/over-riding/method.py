''''
redine a method of method rewrite to child class is called method overrding
same name of method but calling the different object


'''
class A:
    def m1(self):
        print("Welcome to my class")
    def m2(self):
        print("Hellow this is the A class")
a1=A()

class B(A):
    def m2(self):
        print("This is the B class ")

b1=B()
b1.m2()
a1.m2()