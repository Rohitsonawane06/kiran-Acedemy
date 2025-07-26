'''method is function is to perform the opration on the data
    type of method
    1]instance method
        it work on object level data 
        syntax:
            def imethod(self):
                pass
                
            refvar.imethod()
    2]class method
        class method work on class level data to first paramter is cls but the decoratore 
        to access the class method and using the class name to calling 
        the class method
    syntax;
        class method
        @classmethod
        def cmethod(cls):
            pass
            
        classname.methodname()
    3]static method
    it work on local variable data to it work to same like helper functionthe using the staticmethod decorator
    to wrtee the method 
'''

class employee:
    comapnay_name='kiran academy'
    location="pune"
    def __init__(self,id,nm,ag,dep,sal):
        self.id=id
        self.name=nm
        self.age=ag
        self.department=dep
        self.salary=sal

    def emp_details(self):
        return f'''
        id :{self.id}
        Name :{self.name}
        Age : {self.age}
        Department :{self.department}
        Salary : {self.salary}
 '''
    def increment(self,incr_sal):
        inr=self.salary*incr_sal/100
        self.salary=self.salary+inr
        return 'done'
    @classmethod
    def clmethod(cls):
        return f'''
            company name : {cls.comapnay_name}
            location : {cls.location}    
        '''
    @staticmethod
    def cal(salary,inc_per):
        inc=salary*inc_per/100
        return inc
    

e1=employee(101,'vijay',22,'hr',600000)
e2=employee(102,'santosh',22,'opratin',500000)
# print(e1.emp_details())
# print(e1.increment(10))
# print(e1.emp_details())
# print(employee.clmethod())
print(e1.cal(20000,7))
