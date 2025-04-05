'''
Abstract class is considered as a blueprint for other classes 
ABstract class :
    A class which contains one or more basic abstract methods is called an abstract class.
    An abstract method is a method that has a declaration but does not have implementation
'''

from abc import ABC, abstractmethod         # ABC stands for Abstraction class that is used for abstraction

class Help4code(ABC):
    @abstractmethod
    def training(self):
        pass
        
    @abstractmethod
    def placement(self):
        pass
    
class Ashish(Help4code):
    def training(self):
        print("C, C++, Java")
    def placement(self):
        print("Java Placement")
        
class Ankush(Help4code):
    def training(self):
        print("Python|Django")
    def placement(self):
        print("Python Placement students")

class Prashant(Help4code):
    def training(self):
        print("Machine Learning")
    def placement(self):
        print("Data Science Placement")
        
# obj1 = Ashish()
# obj1.training()
# obj1.placement()
# obj2 = Ankush()
# obj2.training()
# obj2.placement()
# obj3 = Prashant()
# obj3.training()
# obj3.placement()

'''
Encapsulation:
    process of protecting the data and functionality in a single unit
    variables can be protected by by marking them as private
    use _ before a variable or method to make it protected
    use __ before a varialbe or methos to make it private
'''

class Base :
    def __init__(self):
        print("Parent class constructer called")
        self.a = "prashant"
        self.__c = "Ashish"
        
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling the private member of the base class : ")
        print(self.a)
        print(self.__c)
        
# obj1 = Derived()
# print(obj1.a)
# print(obj1.__c)
# obj2 = Base()
# print(obj2.__c)

class Rbi:
    def publicproperty(self):
        print("Check the public policy")
    
    def __privatePolicy(self):
        print("There is some private policy which is not accessible for public")
        
class Sbi(Rbi):
    def __init__(self):
        super().__init__()
        
    def callingPublicMethod(self):
        print("\nInside the child class")
        self.publicproperty()
        
    def callingPrivateMethod(self):
        self.__privatePolicy()
        
obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
obj1.publicproperty()
obj1.__privatePolicy()
# obj2 = Rbi()
# obj2.publicproperty()
# obj2.__privatePolicy()