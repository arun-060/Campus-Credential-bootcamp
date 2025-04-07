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
            
    def addNodeAtPos(self,value,position):
        node = Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else : 
            current = self.head
            i = position-1
            while i != 0:
                current = current.next
                i -= 1
            node.next = current.next
            current.next = node
        
if __name__ == "__main__":
    object = LinkedList()
    
    while True:
        print("\n1.Add node of linked list : ")
        print("2.Add Node in begining : ")
        print("3.Add node in between : ")
        print("4.Add node in end : " )
        print("5.Display linked list : ")
        print("6.Add node before position : ")
        print("7.Add node after position : ")
        print("8.Exit")
        
        ch = int(input("Enter your choice : "))
        if ch == 1:
            value = int(input("Enter the value for node : "))
            object.addNode(value)
            print("node added successfully in linked list: ")
        elif ch == 3:
            value = int(input("Enter the value for node : "))
            position = int(input("Enter the position : "))
            object.addNodeAtPos(value,position)
        elif ch == 5:
            object.display()
        elif ch == 2:
            value = int(input("Enter the value for node : "))
            object.addBegining(value)
            print("Value added at the begining")
        elif ch == 4:
            value = int(input("Enter the value of node : "))
            object.addNode(value=value)
        elif ch == 6:
            value = int(input("Enter the value for node : "))
            position = int(input("Enter the position : "))
            object.addNodeAtPos(value,position-1) 
        elif ch == 7:
            value = int(input("Enter the value for node : "))
            position = int(input("Enter the position : "))
            object.addNodeAtPos(value,position+1) 
        else:
            sys.exit()