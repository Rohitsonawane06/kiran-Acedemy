from datetime import date
class bank:
    bank_name='Bank Of Maharashtra'
    branch='Karve Nagar'
    ifsc_code='MAHB000666'
    def __init__(self,nm,ct,ac,bal):
         self.name=nm
         self.city=ct
         self.acc_no=ac
         self.balance=bal

    def check_bal(self):
         return f"Your Bank Balance is :{self.balance}"
    def credit(self,amount):
         if amount>0:
            self.balance=self.balance+amount
            return f'your account number is:xxxxx{str(self.acc_no)[-3:]} is creadit by :{amount} on the date{date.today()} your current balance is {self.balance}'
         else:
             return 'Enter the postive amount'
         
    def debited(self,amount):
         if amount<self.balance:
            self.balance=self.balance-amount
            return f'your account number is:xxxxx{str(self.acc_no)[-3:]} is debited by :{amount} on the date{date.today()} your current balance is {self.balance}'
         else:
             return 'Insufficent funds'
         
    def bank_details(self):
        return f''' Your Bank Name is:{self.bank_name} 
                    the bank address is:{self.branch}
                    Bank IFCE CODE Is : {self.ifsc_code}'''
    @staticmethod
    def simple_Interset(amount,r,y):
        si=amount*r*y/100
        return si
    @staticmethod
    def compound_interset(principle,r,t):
        account=principle*(pow((1+r/100),t))
        CI=account-principle
        return CI
bank_customer=bank('rohit','pune',1234567101,50000)

print(bank_customer.compound_interset(10000,10.25,5))