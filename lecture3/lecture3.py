# # write a program to compress a string by replacing consecative characters with their counts

# string = "aaabbbcccc"
# count = 0

# for i in range(0, len(string)-1):
#     if string[i] == string[i+1]:
#         count += 1
#     else:
#         count += 1
#         print(string[i],count,end=" ")
#         count = 0
# count += 1
# print(string[i],count,end=" ")

# myset={1,2,"sanjay", 5.66,"rahul", "ayaush", "ramesh", "ankit"}
# print(myset)    # always prints data in random order
# # print(myset[0]) # Error : Set object is not subscriptable

# #use add method to add data to the set. the data is added is at the random position
# myset.add(68)
# print(myset)

# myset.discard(3)  # removes the value if it is present if the value is not found the then no error is returned
# print(myset)

# myset.remove(3)   # if the the value is found it is removed else returns keyError
# print(myset)

# myset = {10,20,30,40}
# yourset = {"prashant", "jha"}

# newset = myset.union(yourset)   # use union method to combine both the sets. mathematical union for set is performed
# print(newset)                   # output for the set is printed in random order

# myset = {10,20,30,40}
# yorset = {10,50,60,30}
# print(myset.intersection(yorset)) # use intersection for find the comman elements between the sets

# print(myset.difference(yorset))   # returns the element that is myset but not in yorset

# print(myset.pop())                # removes the last element
# print(myset.clear())              # clear the entire set

# mydict = {
#     101: "prahsant",
#     102:"ashish",
#     "103":"mohini",
#     "104":"trivani",
#     101:"ashish",           # most recent value of the key is updated
#     104:"ashish"
# }
# print(mydict)


# a = mydict[102]
# print(a)

# mydict[102] = "peter"       # for updating the value
# print(mydict) 

# for x in mydict:            # keys are printed
#     print(x)
    
# for x in mydict.values():   # values can be printed by using values() method
#     print(x)
    
# for x, y in mydict.items(): # items() method can be used for printing both the key and values
#     print(x,y)
    
# mydict["mobile_number"] = 102398109823
# print(mydict)

# mydict.pop(101)             # use pop method to remove the pair form the dictionary
# print(mydict)

# newdict = mydict.copy()     # copy method is used to copy the dictionay 
# print(newdict)

# mydict = {
#     "A":10,
#     "B":20,
#     "C":30,
#     "D":40
# }
# sum = 0
# for _, x in mydict.items():
#     sum += x

# print(sum)


# mydict = {"C":3,"B":2,"A":1}
# for key in sorted(mydict):
#     print(key, ":" ,mydict[key])    
   
   
# find the largest number in dictionary 
# mydict = {'A':10,"B":20,"C":30,"D":40,"E":50}
# max = mydict['A']

# for value in mydict.values():
#     if value > max:
#         max = value
# print(max)

# def login():
#     username = input("Enter the username : ")
#     password = input("Enter the password : ")
#     if username == password:
#         print("Login Successful")
#     else :
#         print("invalid credential")
        
# login()

# positional argument
# def info(firstname,lastname):
#     print("first name =",firstname)
#     print("last name =",lastname)
    
# info("prashant", "jha")

# def arithematic(a,b):
#     r = a+b
#     n = a*b
#     m = a-b
#     return r,n,m

# result = arithematic(10,5)
# print("result =", result)

# def func(fname,lname):
#     print("Hi",fname)
#     print("Hi",lname)
# # func(fname="prashant",lname="jha")
# fname=input("Enter the fname :" )
# lname=input("Enter the lname " )
# func(fname,lname)

# def nameofcity(*city):
#     print('Name of the city : ', city)
    
# nameofcity('Mumbai', "Pune", 'Nagpur','Nashik')

# def cityName(city="Napur"):
#     print("city=",city)
    
# cityName('Mumbai')
# cityName('Delhi')
# cityName()

# import module1 as mod

# mod.square(4)
# mod.login('user','user')
# print(mod.pi)
# mod.welcome('prashant','jha')

# from module1 import *

# print(pi)
# square(4)
# login("user","user")

# from math import *

# print(int(sqrt(16)))
# print(ceil(10.1))
# print(floor(10.1))
# print(fabs(-10.6))
# print(fabs(10.6))

from random import *

# for i in range(5):
#     print(random())
    
# # to generate random number between 2 numbers
# for i in range(5):
#     print(randint(1,100000))

# # to return a random float number    
# for i in range(5):
#     print(uniform(1,10))
    
# to return a random element form list
# list = ["pprashant", "rahul", "ashish", "sandip", "sunil"]
# for i in range(10):
#     print(choice(list))
    
# l = [
#     [100,198,323,333],
#     [122,232,221,111],
#     [223,565,245,764]
# ]
# newlist=[]
# for i in range(3):
#     j = 0
#     max = l[i][j]
#     for j in range(4):
#         c_max = l[i][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
    
# print(newlist)

''''
Exception handling
'''

# try :
#     a = int(input("Enter the first value : "))
#     b = int(input("Enter the second value : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
# else :
#     print("this are no errors in try block")
# finally:
#     print("I will always execute")
    
# try:
#     a = int(input("Enter the first value : "))
#     b = int(input("Enter the second value : "))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)

n = '1122334455'
key = 0

for i in n: 
    if n.count(i) > 1:
        key += 1/n.count(i)

print(int(key))

'''
File handling in python
methods :
    open() to open the file along with the mode such as w for write, r for read, a for append
    write() to update the file content if mode is write data will be overridden if the mode is append data will be added
    close() to close the file 
    readable() to check weather the file is readable or not
    writable() to check weather the file is writable or not 
    closed to check weather the the file is closed or not
    user writelines to write into the file with w as a mode
'''

# f = open("myfile.txt","w")
# print("name of the file : ",f.name)
# print("file mode        : ", f.mode)
# print("readable         :",f.readable())
# print("writable         :",f.writable())
# print("file close       :",f.closed)
# f.close()
# print("file closed      :", f.closed)

# mylist = ("prashant","mahesh","suresh")
# mydict = {
#     1:"Ironman",
#     2:"spiderman",
#     3:"thor",
#     4:"Batman"
# }
# f = open("myfile.txt","w")
# f.writelines(str(mydict))
# # print(f.readline())
# f.close()

# f = open("myfile.txt", "r")
# print(f.read())
# f.close()

# with open("myfile.txt",'w') as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("Prashant\n")
#     print("File closed : ", f.closed)
# print("File closed : ", f.closed)

# with open("myfile.txt", "r") as f:
#     content = f.read()
#     print(content)

# f1 = open("blackhole.jpg", "rb")
# f2 = open("new_blackhole.jpg", "wb")

# data = f1.read()
# f2.write(data)
# print("New image is available with the name : ", f2.name)

import csv

f = open("student.csv", "a", newline='')
a = csv.writer(f)
# a.writerow(["studentId", "rollno", "name","mobile no", "email id", "p1",'p2','p3', "total",'percentage', "result"])
# studentId = int(input("Enter student id : "))
# rollno = int(input("Enter your roll no : "))
# name = input("Enter the name : ")
# mobile_no = int(input("Enter mobile number : "))
# email = input("Enter email : ")
# p1 = int(input("Enter paper 1 marks : "))
# p2 = int(input("Enter paper 2 marks : "))
# p3 = int(input("Enter paper 3 marks : "))
# total = p1+p2+p3
# percentage = total/3

# if p1 > 40 and p2 > 40 and p3 > 40:
#     result="pass"
# else:
#     result="fail"
# a.writerow([studentId, rollno, name,mobile_no, email, p1,p2,p3,total,percentage,result])
# print("Changes made")
f1 = open("student.csv", 'r')
b = csv.reader(f1)
data = []

for r in b:
    data.append(r)
    
Id = input("Enter the Id for search : ")
student_data=[]
for i in data:
    if i[0] == Id:
        student_data=i
        
for i in range(len(student_data)):
    print(student_data[i], end="  ")
        
f1.close()