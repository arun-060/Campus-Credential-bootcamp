'''
Tree : it is a non linear data structure with hierarchical relationship between its elements without having any cycle,
it is basically reversed from a real life tree
'''

'''
root : top node without parent
edge : a link between parent and node
leaf : leaf that does not have children
sibling : children of the same parent
ancestor : parent. grandparent, great grandparent of node
depth of node : a length of the path form root to node
height of node : a lenght of the path from the node to the deepest node
depth of tree : depth of root node
height of tree : height of root node
'''

'''
                                                    drink
                                                      |
                                      ---------------------------------
                                     |                                 |
                                    hot                              cold
                                     |                                 |
                             -------------------               ---------------
                            |                   |             |               |
                            tea               coffee    non-alcoholic      alcoholic  
'''

class Tree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None 
        self.rightChild = None 
    
    def __str__(self,level=0):
        ret = "    "*level + str(self.nodeValue) + "\n"
        for child in self.treeList:
            ret += child.__str__(level+1)
        return ret
    
    def addChildNode(self, value):
        self.treeList.append(value)
            
        
rootNode = Tree('Drink')
Hot = Tree("Hot")
Cold = Tree("Cold")
Tea = Tree("Tea")
Coffee = Tree("Coffee")
Alcoholic = Tree("Alcoholic")
NonAlcoholic = Tree("Non-Alcoholic")
rootNode.addChildNode(Hot)
rootNode.addChildNode(Cold)
Hot.addChildNode(Tea)
Hot.addChildNode(Coffee)
Cold.addChildNode(NonAlcoholic)
Cold.addChildNode(Alcoholic)
# print(rootNode)

'''
Types:
    full binary tree :
        either 0 or 2 children no single child 
    Compelte binary tree :
        all level except possibly the last are completely filled
        node in the last level are filled from left to right
    perfect binary tree : 
        all internal nodes have exactly two nodes
        all leaf node are at the same level
    balanced binary tree :
        the difference between the height of the left and right subtree of any node is not more than one
'''                            

# '''
# 5
# 10 11 7 12 14
# output 12
# '''
# arr = [10,11,7,12,14]
# sum = 0
# for i in range(len(arr)-1):
#     sum += abs(arr[i]-arr[i+1])
    
# print(sum)
# string="gasgg55@#vscd!s*"
# count = 0

# for i in string:
#     if i.isalnum():
#         continue
#     else:
#         count += 1
        
# print(count)
        

  