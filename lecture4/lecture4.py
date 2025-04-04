class Student:                                      # use class to define a class
    roll_number = 101                               # data members
    num1 = 50
    num2 = 100
    
    def add(self):                                  # member function
        print(self.num1 + self.num2)
        self.name = input("Enter name : ")
#         print(self.name)

# obj = Student()                                     # creating an object
# obj.add()                                           # calling the method
# print(obj.roll_number)                              # calling the variable

class NewClass:
    def __init__(self):                                                 # creating constructor
        print("my name is constructor i will always execute first")
    
    def show(self):
        print("welcome to the class level programming")
        
# obj = NewClass()
# print(obj)
# obj.show()

class Hod:
    def __init__(self, name,age, rollno):
        self.name = name
        self.age = age
        self.empId = rollno
        
    def info(self):
        print("My name is : ", self.name)
        print("My age is : ", self.age)
        print("My emp id is : ", self.empId)

# obj = Hod("Arunkumar", "23", 17)
# obj.info()

class New:
    def __init__(self):
        self.a = 10             # this type of vairalble is called instance variable it is defined for every object created using this class
        
# obj1 = New()
# obj2 = New()
# obj3 = New()
# obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

class Student:
    def __init__(self):
        self.s_name = "prashant"
        self.l_name = "jha"
        self.roll_no = 101
        
    def getdata(self):
        self.s_mb = 8973598730
        
# obj = Student()
# obj.getdata()
# obj.s_branch = "CS"  # initializing the instance variable by using object
# print(obj.__dict__)  # __dict__ is a method used to return the data members in the dictionary format
# print(obj.s_mb)

# class College:
#     collegename = "Modern College"

#     def __init__(self):
#         self.studentname = "prashant"
        
# principal = College()
# tracher = College()
# accountant = College()

# print("principal=",principal.collegename,"...",principal.studentname)
# print("teacher=",tracher.collegename,"...",tracher.studentname)
# print("accountant=",accountant.collegename,"...",accountant.studentname)

# College.collegename = "HBD"
# principal.studentname="prashant jha"

# print("principal=",principal.collegename,"|",principal.studentname)
# print("teacher=",tracher.collegename,"|",tracher.studentname)
# print("accountant=",accountant.collegename,"|",accountant.studentname)

'''
declaring the static variable
    insider a class but outside of the method
    in a constructor by using class name
    in a instance using class name or cla varialbe
    stativ method by using name
how to access static variable
    insider instance method using self or class name
    in a constructor using self or class name
    in a class method usign cls variable or class name
    in a static method using class name
    outside of the class using object or class name
how to delete the static variable
    del classname.Static_varialbe_name
'''

# import sys
# class CRUD:
#   def __init__(self):
#     print('Student Management System')
#     self.studentID=[]
#     self.studentName=[]
#     self.studentRollNo=[]
#     self.studentCity=[]

#   def addStudent(self):
#     self.studentID.append(int(input('Enter Student ID: ')))
#     self.studentName.append(input('Enter Student Name: '))
#     self.studentRollNo.append(int(input('Enter Student Roll No: ')))
#     self.studentCity.append(input('Enter Student City: '))

#   def deleteStudent(self,id):
#     a=input('Do you really want to delete the record(y/n): ')
#     if a=='y':
#       if id in self.studentID:
#         i=self.studentID.index(id)
#         self.studentID.pop(i)
#         self.studentName.pop(i)
#         self.studentRollNo.pop(i)

#   def showStudent(self):
#     print('Student ID\tStudent Name\tStudent Roll No\tStudent City')
#     for x in range(60):
#       print('-',end='')
#     print()
#     for i in range(len(self.studentID)):
#       print(f"{self.studentID[i]:<10}\t{self.studentName[i]:<20}\t{self.studentRollNo[i]:<15}\t{self.studentCity[i]:<15}")
#     for x in range(60):
#       print('-',end='')
#     print()

#   def updateStudent(self):
#     newstudentID=int(input('Enter Student ID: '))
#     for i in range(len(self.studentID)):
#       if newstudentID==self.studentID[i]:
#         print('Matched student Data are: ')
#         print('1 Student Roll No: ',self.studentRollNo[i],'\n2 Student Name: ',self.studentName[i],'\n3 Student City: ',self.studentCity[i],'\n4: Dont want to update')
#         ch=int(input('Enter your choice: '))
#         if ch==1:
#           self.studentRollNo[i].insert(i,input('Enter New Student Roll No: '))
#         elif ch==2:
#           self.studentName[i].insert(i,input('Enter New Student Name: '))
#         elif ch==3:
#           self.studentCity[i].insert(i,input('Enter New Student City: '))
#         elif ch==4:
#           pass
#         print('Data updated')
# obj=CRUD()
# while True:
#   print('1.Add Student')
#   print('2.Delete Student')
#   print('3.Show Student')
#   print('4.Exit')
#   ch=int(input('Enter your choice: '))
#   if ch==1:
#     obj.addStudent()
#   elif ch==2:
#     id=int(input('Enter Student ID: '))
#     obj.deleteStudent(id)
#   elif ch==3:
#     obj.showStudent()
#   elif ch==4:
#     break

'''
inheritance : expanding the property form one class to another class is called inheritance

types of inheritance :
    single inheritance
    multilevel inheritance
    multiple inheritance
''' 

'''
Single inheritance
'''

# class Collage:
#     def college_name(self):
#         print("Modern College")

# class Student(Collage):
#     def student_info(self):
#         print("Name : Prashant jha")
#         print("Branch : Mechanincal")

# obj = Student()
# obj.college_name()
# obj.student_info()


'''
Multilevel inheritance
'''

# class Collage:
#     def college_name(self):
#         print("Modern College")

# class Student(Collage):
#     def student_info(self):
#         print("Name : Prashant jha")
#         print("Branch : Mechanincal")

# class Exam(Student):
#     def subject(self):
#         print("Subject1 : DEsing engineering")
#         print("Subject2 : Math")
#         print("Subject3 : c-language")

# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()


'''
Multiple inheritance
'''

# class SubjMarks:
#     math = int(input("Enter the math marks : "))
#     DE = int(input("Enter paper marks of desing Engineering : "))
#     c = int(input("Enter the paper marks of c language : "))
#     english = int(input("Enter paper marks of english : "))
    
# class PractMarks:
#     cpract = int(input("Enter the practical marks of c langauge : "))
    
# class Result(SubjMarks, PractMarks):
#     def total(self):
#         if self.math >= 40 and self.c>= 40 and self.english >= 40 and self.cpract >= 40:
#             print("pass")
#         else :
#             print("fail")
            
# obj = Result()
# obj.total()

# class A:
#     def add(self):
#         print(2+2)

# class B:
#     def add(self):
#         print(3+3)
        
# class C(A,B):
#     def display(self):
#         print("msg display")

# obj = C()
# obj.add()

'''
polymorphism : having many forms
compile time polymorphism : function overloading
runtime polymorphism : function overriding

python does not support function overloading and method overloading 

'''


# class Arithematic:
#     def add(self, a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
        
# obj = Arithematic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

# class Arithematic:
#     def add(self,a=None,b=None,c=None):
#         if a != None and b!=None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print("enter the atlest two argument")
            
# obj = Arithematic()
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)

'''
constructor overloading is not supported in python 
'''

# class Arithematic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self, a):
#         print("There is one argument")
#     def __init__(self,a,b):
#         print("There is two argument")
        
# obj = Arithematic()
# obj = Arithematic(20)
# obj = Arithematic(10,20)

# class Deposit:
#     def __init__(self,cash):
#         self.cash = cash
#     def __add__(self,other):
#         return Deposit(self.cash + other.cash)
#     def __str__(self):
#         return str(self.cash)
        
# d1=Deposit(1000)
# d2=Deposit(2000)
# d3=Deposit(2000)
# print(d1+d2+d3)

'''
method overriding
'''

# class RBI:
#     def homeLoan_ROI(self):
#         print("Home load roi = 7.5%")
        
#     def carLoan_ROI(self):
#         print("car loan roi = 8%")
        
# class SBI(RBI):
#     def homeLoan_ROI(self):
#         print("home load roi = 6.5%")
#         return super().homeLoan_ROI()        # user super() to use the parent class method after overloading
        
# obj = SBI()
# obj.homeLoan_ROI()
# obj.carLoan_ROI()

# class Father:
#     def __init__(self):
#         print("Father := i am allready at the breakfast table")

# class Child(Father):
#     def __init__(self):
#         print("Child:= i will be late for breakfast")                          # chlid class constructer is considered after inheritance
#         super().__init__()                                                     # use super to call the parent class constructer
        
# obj = Child()

# a = {
#     (1,2):1,
#     (2,3):2,              
#     (4,5):3
# }
# print(a[4,5])             # here key is a tuple hence the value is returened

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])           # here every value has single key hence only one key is accepted thus keyError

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else :
#         fruit[index] = 1
# addone("Apple")
# addone("banana")
# addone("apple")
# print(len(fruit))

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# mydict = {}
# mydict[(1,2,4)] = 8
# mydict[(4,2,1)] = 10
# mydict[(1,2)] = 12
# sum = 0
# for k in mydict:
#     sum+=mydict[k]
# print(sum)
# print(mydict)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars["jam"] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates))

# dict = {'c':97,'a':96,'b':98}

# for i in sorted(dict):
#     print(dict[i])

rec = {'name':"python","age":20}
id1 = id(rec)
del rec
rec = {'name':"python","age":20}
id2 = id(rec)
print(id1 == id2)