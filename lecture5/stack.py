'''
Data structure : different way of organizing data on computer that can be effictiverly used
'''

'''
Data structure:
    primitive :
        INTEGER
        FLOAT
        CHARACTER
        STRING
        BOOLEAN
    non-primitive:
        linear :

        non-linear :

'''

'''
stack implementation without size:
    1. psuh
    2. pop
    3. peek
    4. isEmpty
    5. isFull
    6. Delete
    7. Display
'''

import sys

class Stack :
    def __init__(self, size):
        self.stackSize = size
        self.myStack = []            # in python represent the stack usign list data structure
    
    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else :
            return False
    
    def push(self,data):             # insert the element to the top of the stack 
        if self.isFull():
            print("stack is full")
        else :    
            self.myStack.append(data)
            print("push element is done")
        
    def displayStack(self):          # print the stack
        print(self.myStack) 
    
    def pop(self):                   # remove top element from the stack
        if self.isEmpty():
            print("stack is empty")
        else:
            print("the element pop:", self.myStack.pop())
        
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else :
            print("The top element : ", self.myStack[-1])
        
    def isEmpty(self):
        if self.myStack == []:
            return True
        else :
            False
    
    def deleteStack(self):
        self.myStack = None
        print("stack is deleted")

size = int(input("enter the size of stack : "))
obj = Stack(size)
print("stack has created:")

if __name__ == "__main__":
    while True:
        print("1.push operation : ")
        print("2.pop operation : ")
        print("3.peek operation : ")
        print("4.isEmpty operation : ")
        print("5.display operation : ")
        print("6.delete operation : ")
        print("7.Exit")
        print()
        ch = int(input("Enter your choice : "))
        
        if ch == 1:
            data = int(input("Enter the element for the stack : "))
            obj.push(data)
        elif ch == 2:
            obj.pop()
        elif ch == 3:
            obj.peek()
        elif ch == 4:
            print(obj.isEmpty())
        elif ch ==5:
            obj.displayStack()
        elif ch == 6:
            obj.deleteStack()
        elif ch == 7:
            sys.exit()
