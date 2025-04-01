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
    
n1 = int(input("num1 : "))
n2 = int(input("num2 : "))
n3 = int(input("num3 : "))
n4 = int(input("num4 : "))
n5 = int(input("num5 : "))

if n1 >n2 and n1 > n3 and n1 > n4 and n1 > n5 : 
    print("n1 is the greatest")
if n2 >n1 and n2 > n3 and n2 > n4 and n2 > n5 : 
    print("n2 is the greatest")
if n3 >n2 and n3 > n1 and n3 > n4 and n3 > n5 : 
    print("n3 is the greatest")
if n4 >n2 and n4 > n3 and n4 > n1 and n4 > n5 : 
    print("n4 is the greatest")
if n5 >n1 and n5 > n2 and n5 > n3 and n5 > n4 : 
    print("n5 is the greatest")