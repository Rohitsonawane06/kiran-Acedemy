''''
same variable but  different value  in child class to using parent class variable name is called variable overding

'''

class bank:
    def __init__(self,nm,acc,bal):
        self.name=nm
        self.account_no=acc
        self.balance=bal
    def credit(self,amount):
        if amount>0:
            self.balance+=amount
            return 'your account is credited'
        else:
            return 'inavalid amount'
    def debited(self,amount):
        if amount<=self.balance:
            self.balance+=amount
            return ' your account is bedited'
        else:
            return 'insufficant balance '
    def check_balance(self):
        return f'your balance is :{self.balance}'
    
class saving_ac(bank):
    rate_of_intereset=5
    def __init__(self, nm, acc, bal,adh):
        super().__init__(nm, acc, bal)
        self.adhar=adh
   
    def interset(self):
        si=self.balance*saving_ac.rate_of_intereset/100
        si+=self.balance
        print(f'you intersert succsfully done by {si}')

class current_acc(bank):
    def __init__(self, nm, acc, bal,ol):
        super().__init__(nm, acc, bal)
        self.overdraft=ol
    def debited(self, amount):
        if amount<=self.balance+self.overdraft:
            self.balance-=amount
            return 'done'
        else:
            return 'insufficant balance '

s1=saving_ac('rohit',10323239101,20000,509915191459)
c1=current_acc('vijay',10381238102,20000,5000)
print(c1.debited(24000))