class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
    def __str__(self,level=0):
        ret = "    "*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
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
    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
newBT.leftChild = leftChild
NonAlcoholic = TreeNode("Non-Alcoholic")
Alcoholic = TreeNode("Alcoholic")
rightChild.rightChild = Alcoholic
rightChild.leftChild = NonAlcoholic
newBT.rightChild = rightChild


def pre_order_traversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    pre_order_traversal(rootNode.leftChild)
    pre_order_traversal(rootNode.rightChild)
    
print("\npre order traversal : ")
pre_order_traversal(newBT)

def in_order_traversal(rootNode):
    if not rootNode:
        return
    in_order_traversal(rootNode.leftChild)
    print(rootNode.data)
    in_order_traversal(rootNode.rightChild)
    
print("\nin order traversal : ")
in_order_traversal(newBT)

def post_order_traversal(rootNode):
    if not rootNode:
        return
    post_order_traversal(rootNode.leftChild)
    post_order_traversal(rootNode.rightChild)
    print(rootNode.data)

print("\npost order traversal : ")
post_order_traversal(newBT)

def level_order_traversal(rootNode):
    if not rootNode:
        return
    
    nodes = [rootNode]
    while len(nodes)>0:
        curr = nodes.pop(0)
        print(curr.data, end = " ==> ")
        
        if curr.leftChild is not None:
            nodes.append(curr.leftChild)
            
        if curr.rightChild is not None:
            nodes.append(curr.rightChild)
            
print("\nlevel order traversal : ")
level_order_traversal(newBT)
