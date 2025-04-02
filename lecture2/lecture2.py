# mylist = ["prashant", "Ashish","komal", "ankush", "Ashish", 77,"Sandip",60,52,"prashant"]
# print(mylist)
# print(mylist[0])
# print(mylist[1])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])

# mylist[0] = "Arun"
# print(mylist)

# if "ankush" in mylist:
#     print("yes ankush is avilable")
# else:
#     print("not avilable")

# mylist.append("harsh")
# mylist.append("laxman")
# print(mylist)

# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("prashant")
# print(mylist)

# newlist = mylist.copy()
# print(newlist)

# mylist = [["prashant", "jah"], [85.56], [440022, "yyy"]]

# print("Example of multidimensional list : ")
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1 = ["prashant", "jha"]
# print(list1)

# list2 = [50,25,50]
# print(list1+list2)

# list2 = [50,25,50,"prashant"]
# del list2
# del list2[2]
# print(list2)

# list2.clear()
# print(list2)

# name = "prashant"
# print(name)
# myname=list(name)
# print(myname)

# mylist=[40,30,20,10]
# mylist.reverse()
# print(mylist)

# mylist = [44,22,77,0,9,88]
# mylist.sort(reverse=True)
# print(mylist)

"""
default sorting for the number is ascending and for string is alphabetical order. for sorting list must contaion homegeneous data type
use parameter (reverse = True) to sort in descending order
"""

# newlist = mylist

# print(id(mylist))
# print(id(newlist))

# list1 = [5,3,9,2,8]
# max = min = list1[0]
# for i in list1:
#     if i > max:
#         max = i
#     print(i)

# list1 = [0,0,1,2]
# for i in list1:
#     if i == 0:
#         list1.remove(i)
#         list1.append(0)
# print(list1)

# l1=[1,2,3]
# l2=[2,3,4]
# l3=[3,4,5]

# for i in l1:
#     if i in l1 and i in l3:
#         print("intersection =",i)

# mycart=[10,20,200,300,800.60,700]

# for i in mycart:
#     if i>400:
#         print("my cart")
#         continue
#     print(i)

# for i in range(1,6):
#     if i == 3:
#         continue
#     else:
#         print(i, 6-i)
        
"""zip() function can use multiple range function"""

# above program using zip function

# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i == 3 and j ==3:
#         continue
#     print(i, " ", j)

# mycart=[10,20,800,60,70]

# for item in mycart:
#     if item>400:
#         print("not in my budget")
#         continue
#     print(item)
# else:
#     print("Already purchased everything")

# print("Prashant".find("r"))
# print("Prashant".index("r"))
# print("prahsant jha".count("a"))

# val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
# print(val.index(1))
# print(val.index(2))
# print(val.index(3))
# print(val.index(4))
# print(val.index(5))
# print(val.index(6))

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)

# arr = [1,1,0,1,1,1,0,1,1,1,1,0]
# count = 0
# maxcount = 0
# for i in range(len(arr)):
#     if arr[i] == 1:
#         count += 1
#         if count > maxcount:
#             maxcount=count
#     else :
#         count = 0
# print(maxcount)

# arr = [1,2,3,4]
# ele=0
# l = []
# for i in arr:
#     for j in arr:
#         if i != j:
#             i = i+i*j
#             l.append(i)
# print(l)    

# s= "abababababab"
# s1=s.replace("a","b")
# print(s1)

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()
    
# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i), end=" ")
#     print()
    
# n=int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(i,end=" ")
#     print()

# n=int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")
#     print()

# import time

# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(n+1-i, end=" ")
#     print()
# time.sleep(2)

# import time

# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     print(" "*(n-i), end=" ")
#     for j in range(1,i+1):
#         time.sleep(1)
#         print("*",end=" ")
#     print()

# arr = [
#     [1,2,3,4],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12,13,14,15]
# ]

# for i in range(0,4):
#     print(arr[i].pop())

# arr = [1,2,3,4,5,6]

# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i], end = " ")
    
# fl1=['apple','berry','cherry','papya']
# fl2=fl1
# fl3=fl1[:]
# fl2[0]='guava'
# fl3[1]='kiwi'

# sum = 0;
# for ls in (fl1,fl2,fl3):
#     if ls[0] == 'guava':
#         sum+=1
#     if ls[1] == "kiwi":
#         sum+=20
# print(sum)

# i = 1
# while i<6:
#     print(i)
#     if i == 3:
#         pass
#     i = i + 1 

# i = 0
# while i<6:
#     i += 1
#     if i==3:
#         continue
#     print(i)

# username = ''
# password = ' '

# while username != password:
#     username = input("Enter username : ")
#     password = input("Enter password : ")
#     print("Login Succesfull")

# string = input("Enter the string : ").lower()
# vowel = 0
# const = 0
# for c in string :
#     if c in 'aeiou':
#         vowel += 1
#     else :
#         const += 1
# print(vowel,const)

# string1 = input("Enter the first string : ").lower()
# string2 = input("Enter the second string : ").lower()

# if len(string1) == len(string2):
#     for c in string1:
#         for d in string2:
#             if c in string2 and d in string1:
#                 print("Anagram")

# # count a substring
# string = input("Enter the string : ")
# sub = input("Enter the substring : ")
# count = string.count(sub)
      
# print(count)

# string = "Hello world"
# l = string.split(" ")
# newstr = ''
# for i in range(len(l)):
#     newstr = newstr + l.pop() + " "
    
# print(newstr)

# # find the majority element
# a = [3,3,4,2,4,4,2,4,4]
# answer = 0
# count = []
# for i in a:
#     if a.count(i) > len(a)/2 :
#         answer = i
# print(answer)

# mytuple = ("prashant", "ashish", "Rahul")
# print(mytuple)
# print(type(mytuple))

# mytuple[2] = "arun"
# print(mytuple)

# init_tuple = ()
# print(init_tuple.__len__())

# init_tuple_a = 'a','b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a + init_tuple_b)

# init_tuple = [(0,1), (1,2), (2,3)]
# result = sum(n for _,n in init_tuple)
# print(result)

# l = [1,2,3]
# init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
# #                               3        - [3,2,1][0] == 0
# print(init_tuple)

# init_tuple = (1,)*3
# init_tuple[0] = 2        ressign error
# print(init_tuple)

init_tuple = ((1,2), )*7
print(init_tuple)
print(len(init_tuple[3:8]))