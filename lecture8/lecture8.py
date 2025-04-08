'''
input 
6 30 50
29 38 12 48 39 55
output:
38 48 39
'''
input1 = '6 30 50'.split(' ')
input2 = '29 38 12 48 39 55'.split(' ')

def solution(input1,input2):
    for i in range(int(input1[0])):
        if int(input2[i])>int(input1[1]) and int(input2[i])<int(input1[2]):
            print((input2[i]),end=" ")
        
        elif int(input2[i])<-int(input1[1]) and int(input2[i])>-int(input1[2]):
            print((input2[i]),end=" ")
                 
solution(input1,input2)
        