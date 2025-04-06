# import csv

# with open("emp.csv", "w", newline='') as f:
#     w=csv.writer(f)
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     n=int(input("Enter number of employee : "))
#     for i in range(n):
#         eno = input("Enter employee no : ")
#         ename = input("Enter employee name : ")
#         esal = input("Enter employee salary : ")
#         eadd = input("Enter the employee address : ")
#         w.writerow([eno,ename,esal,eadd])
        
# print("total employee data written to csv file successfully")

# f = open('emp.csv','r')
# r=csv.reader(f)
# data=list(r)
# for line in data:
#     for word in line:
#         print(word,"\t", end='')
#     print()

# s = input("Enter some string : ")
# l=s.split()
# print(l)
# l1=[]
# i=0
# while i<len(l):
#     l1.append(l[i][::-1])
#     i=i+1
    
# output = " ".join(l1)
# print(output)

# s=input("Enter some string : ")
# i = 0
# print("Character ar even position: ")
# while i < len(s):
#     print(s[i],end=',')
#     i=i+2
    
# print()

# print("character at odd position : ")
# i = 1
# while i<len(s):
#     print(s[i],end = ",")
#     i=i+2

# n = int(input("enter the number of students : "))
# d = {}
# for i in range(n):
#     name = input("Enter Student Name : ")
#     marks = input("Enter Student Marks : ")
#     d[name]=marks

# while True:
#     name=input("enter student name to get marks : ")
#     marks=d.get(name,-1)
#     if marks == -1:
#         print("student not found")
#     else:
#         print("the marks of ", name,"are",marks)
#     option=input("do you want to find another studnet marks[yes|no] : ")
#     if option=="no":
#         break

s="learning python is very easy"
n=len(s)
i=0
print("Forward direction")
while i < n:
    print(s[i],end=" ")
    i += 1
    
print("Backward direction")
i = -1
while i >= -n:
    print(s[i],end= " ")
    i = i-1
    
    
