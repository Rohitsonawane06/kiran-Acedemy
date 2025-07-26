'''
abstration process of hiding of the implementation details of a class and exposing only essential feature of the useer .
this allows developers to focus on what an object does raather than how it does it


abstract class 
    1]abstract method
    it is only define and not the implementation the method is called a abstration method using the abstratmethod decorate using the tho 
    crate the abstrt method and import the model of the abstractmethod


    interface: all the method are define the abstract method is called the interface 
    2]non abstract method


    

syntax:
from abc import ABC,abstractmethod
class classname(ABC):
    @abstractmethod
   def method_name(self):
    pass
'''
from abc import ABC,abstractmethod
class Rbi(ABC):
    @abstractmethod
    def ifdc_code(self):
        pass
    @abstractmethod
    def crop_loan(self,amount,t):
        pass