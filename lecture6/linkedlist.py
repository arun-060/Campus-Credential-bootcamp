import time
import sys

class Node:
    
    def __init__(self, item):        
        self.item = item
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else :
            self.tail.next = node
            self.tail = node
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.item, " --> ", end="")
            current = current.next
    
    def addBegining(self,value):
        node = Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else :
            node.text=self.head
            self.head = node
        
if __name__ == "__main__":
    object = LinkedList()
    
    while True:
        print("\n1.Add node of linked list : ")
        print("2.Add Node in begining : ")
        print("3.Add node in between : ")
        print("4.Add node in end : " )
        print("5.Display linked list : ")
        print("6.Exit")
        
        ch = int(input("Enter your choice : "))
        if ch == 1:
            value = int(input("Enter the value for node : "))
            object.addNode(value)
            print("node added successfully in linked list: ")
        elif ch == 5:
            object.display()
        elif ch == 2:
            value = int(input("Enter the value for node : "))
            object.addBegining(value)
            print("Value added at the begining")
        else:
            sys.exit()
    
    
    