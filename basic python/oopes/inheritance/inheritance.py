'''
inheritance 
key feature inherit method and properties from parent class ,reducing the need to retwrite the comman funct.
the child class can
inh
syntax:
    class c1:
        pass
        
    class c2(c1):
        pass


'''
# class Xyz:
#     def m1(self):
#         print('this is m1 method of Xyz class')
#     def m2(self):
#         print("This is the m2 method of Xyz class")

# class Abc(Xyz):
#     pass
# a1=Abc()
# a1.m1( )

class bank:
    def __init__(self,nm,num,bal):
        self.name=nm
        self.account_no=num
        self.balance=bal

    def check_balance(self):
        return(f'your bank balance is:{self.balance}')

    def credite(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'your bank account is credited is :{amount} and your current balance is now {self.balance}')
        else:
            print("Please Enter positive amount")
    def debited(self,amount):
        if amount<self.balance:
            self.balance-=amount
            return(f'you amount is debited : {amount} and your current balance is now {self.balance}')
        else:
            return 'insufficant balance'

class saving_account(bank):
    rate_of_intereset=5
    def interset(self):
        si=self.balance*saving_account.rate_of_intereset/100
        si+=self.balance
        print(f'you intersert succsfully done by {si}')

cs=saving_account('rohit',1278101,20000)
# cs.credite(10000)
# print(cs.check_balance())
print(cs.debited(10000))
print(cs.check_balance())
# cs.interset()
# print(cs.check_balance())

'''
types of inhertiance
1]singlr inheritance
syntax:
    class c1:
        pass
        
    class c2(c1):
        pass

2]multi-level inheritance
syntax:
class a:
    pass
class B(A):
    pass
class C(B)

3]mutiple inheritance
single child to mutiple parent class is called mutiple Inheritance
syntax:
class P1:
    pass
class P2:
    pass
class P3:
    pass
class c(P1,P2,P3)


4] herachical Inhertiance
single parent class to mutiplee child to child class is called mutiple inhertiance

Syntax:
class P1:
    pass
class c1(P1):
    pass
class c2(P1):
    pass
class c3(p1):
    pass
'''
class P1():
    def m1(self):
        print('this is the m1 method of P1 class')
class c1(P1):
    def m2(self):
        print('this is the m2 method of c1 class')
class c2(P1):
    def m3(self):
        print('this is the m3 method of c2 class')
class c3(P1):
    def m4(self):
        print('this is the m4 method of c3 class')

a=c1()
a.m1()

b=c2()
b.m1()

c=c3()
c.m1()

'''
hybrid inhertiance
is combination of two or more is called  hybrid inhertiance
the all type are mixed in this inhertiance is called hybrid inhertiance
'''
