# print(float(3))
# print(float(True))
# # print(float(3+4j)) float cannot convert complex data type into float 
# print(float(4.22))
# print(float(4))

# # complex() 
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# # print(complex("Arun")) cannot typecast this type 
# print(complex(5,-3))
# print(complex(True, False))

# # bool()
# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool(""))

# # string slicing
# name = "arunkumar"
# print(name[0])
# print(name[1])
# print(name[-1])
# # print(name[15]) Error : Array index out of range
# print(name[0:5])  # arun
# print(name[1:])   # runkumar
# print(name[:5])   # arun
# print(name[:])    # arunkumar
# print(name[1:8:2])# rnua
# print(name[::-1])

# #Opeartors

# #identity operators
# a = 10
# b = 10
# print (a is b)
# print(a is not b)

# #membership operator
# a = "help4code"
# print('e' in a)
# print('f' not in a)

# # conditinal operator
# number = int(input("Enter any number : "))
# if number > 0 :
#     print("number is positive")
# if number < 0:
#     print("number is negative")
# if number == 0:
#     print("number is 0")
    
# n1 = int(input("num1 : "))
# n2 = int(input("num2 : "))
# n3 = int(input("num3 : "))
# n4 = int(input("num4 : "))
# n5 = int(input("num5 : "))

# if n1 >n2 and n1 > n3 and n1 > n4 and n1 > n5 : 
#     print("n1 is the greatest")
# if n2 >n1 and n2 > n3 and n2 > n4 and n2 > n5 : 
#     print("n2 is the greatest")
# if n3 >n2 and n3 > n1 and n3 > n4 and n3 > n5 : 
#     print("n3 is the greatest")
# if n4 >n2 and n4 > n3 and n4 > n1 and n4 > n5 : 
#     print("n4 is the greatest")
# if n5 >n1 and n5 > n2 and n5 > n3 and n5 > n4 : 
#     print("n5 is the greatest")
    
    
# p1 = int(input("Enter paper-1 marks : "))
# p2 = int(input("Enter paper-2 marks : "))
# p3 = int(input("Enter paper-3 marks : "))
# p4 = int(input("Enter paper-4 marks : "))
# p5 = int(input("Enter paper-5 marks : "))

# total = p1 + p2 + p3 + p4 + p5
# percentage = total/5.0

# if percentage >= 80:
#     print("GRADE : A")
# elif percentage >= 60:
#     print("GRADE B")
# elif percentage >= 40:
#     print("GRADE C")
# else:
#     print("Fail")
    

# gender = input("Enter your gender (Male/Female) : ")

# if percentage >= 60 and gender == 'Male':
#     print("you eligible for placement.")
# if percentage >= 65 and gender == "Female":
#     print("you eligible for placement.")
# else : 
#     print("you are not eligible.")

# print("total", total)
# print("percentage", percentage)

# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))
# c = int(input("Enter the value of c : "))

# if a>b :
#     if a>c :
#         print("A is greater")
#     else : 
#         print("B is greater")
# else : 
#     if b>c :
#         print("B is greater")
#     else :
#         print("C is greater")

# year = int(input("Enter the year : "))

# if (year % 100) == 0:
#     if year % 400 == 0:
#         print("Year is a leap year.")
#     else :
#         print("Year is not a leap year.")
        
# else :
#     if (year % 4) == 0:
#         print("Year is a leap year")
#     else :
#         print("Year is not a leap year.")

# ch = ord(input("Enter the string : "))

# if ch >= 65 and ch <= 90:
#     print("uppercase detected.")
# elif ch >= 97 and ch <= 122:
#     print("lowercase detected")
# elif ch >= 48 and ch <= 57:
#     print("digit detected")
# else:
#     print("Special symbole detected.")

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{j*i:4}", '  |' ,end = " ")
#     print()
# print("------------------------------------------------------------------------------------------------")
# for i in range(11,21):
#     for j in range(1,11):
#         print(f"{j*i:4}", '  |' ,end = " ")
#     print()

# count = 0
# for i in range(9):
#     if i%2 == 0:
#         print(i)
#     else :
#         print(i)
#         count += 1
# print("count = ", count)

# s = "help4code is a best platform for practicing progamming"
# print(s.find('help4code'))
# print(s.find('python'))
# print(s.find("progamming"))

# s = "prashant","ashish","sandip"
# m = '*'.join(s)
# print(m)

# s = "Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# phy = 50
# chem = 60
# math=70
# print("physics = {} chenistry = {} Math = {}".format(phy,chem,math))
# print("physics = {0} chenistry = {1} Math = {2}".format(phy,chem,math))
# print("physics = {x} chenistry = {y} Math = {z}".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total marks",f"{total}")
# print("Roll no=","7".zfill(4))

print('prashantjha777'.isalnum())
print('prashantjhs'.isalpha())
print('777f'.isdigit())
print('sdsdsd'.islower())
print(''.islower())
print('PRAh'.isupper())
print("PRASH".isupper())
print('My Name Is Prashant'.istitle())
print(''.istitle())
print(''.isspace())
print("Hello".startswith("He"))
print("Hello".endswith("lo"))