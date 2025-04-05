'''
Queue implementation with/without size

'''

import sys

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def isFull(self):
        if len(self.queue) == self.size:
            return True
        else :
            return False
    
    def isEmpty(self):
        if self.queue == []:
            return True
        else :
            False
            
    def display(self):
        print(self.queue)
        
    def enqueue(self,data):
        if self.isFull():
            print("queue is full")
        else :
            self.queue.insert(0,data)
        
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        
        else:
            del self.queue[0]
        
    def delete(self):
        self.queue = []
        
size = int(input("enter the size : "))
obj = Queue(size)

if __name__ == "__main__":
    while True:
        print("1.enqueue operation : ")
        print("2.dequeue operation : ")
        print("3.peek operation : ")
        print("4.isEmpty operation : ")
        print("5.display operation : ")
        print("6.delete operation : ")
        print("7.isfull")
        print("8.Exit")
        print()
        ch = int(input("Enter your choice : "))
        
        if ch == 1:
            data = int(input("Enter the element for the stack : "))
            obj.enqueue(data)
        elif ch == 2:
            obj.pop()
        elif ch == 3:
            obj.dequeue()
        elif ch == 4:
            print(obj.isEmpty())
        elif ch ==5:
            obj.display()
        elif ch == 6:
            obj.delete()
        elif ch == 8:
            sys.exit()
