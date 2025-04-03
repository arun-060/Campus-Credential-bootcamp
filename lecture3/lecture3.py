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

from module1 import pi,square,login

print(pi)
square(4)
login("user","user")
