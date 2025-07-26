from abstrationex import Rbi
class Sbi(Rbi):
    crop_loan_rate=8
    def ifdc_code(self):
        return 'SBIN000978'
    
    def crop_loan(self, amount, t):
       return amount*Sbi.crop_loan_rate*t/100 
    
    
s1=Sbi()
print(s1.ifdc_code())