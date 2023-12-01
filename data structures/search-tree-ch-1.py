class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def printTree(rootNode):
    if rootNode is not None:
       printTree(rootNode.left)
       printTree(rootNode.right)
       print(rootNode.value)

def checkHelper(node, baseValue, Subtree):
    #declaring the smallestValue again


    #check if we could return False based of the node and its children
    if (node.left is not None and node.left.value >  node.value) or (node.right is not None and node.right.value < node.value):
        return False
    
    #check if it collides with the value of the root node
    if (Subtree == "right" and ((node.left is not None and node.left.value < baseValue) or (node.right is not None and node.right.value < baseValue))) or (Subtree == "left" and ((node.left is not None and node.left.value > baseValue) or (node.right is not None and node.right.value > baseValue))):
        return False

    #continue with the recursion if possible
    if node.right is not None:
        checkHelper(node.right, baseValue, Subtree)
    if node.left is not None:
        checkHelper(node.left, baseValue, Subtree)
    
    #if everything cheks out return true
    return True

def checkIfBSTIsBalanced(rootNode):
    if rootNode is None:
        return True

    #check if we could return False
    if rootNode.right is not None and rootNode.right.value < rootNode.value:
        return False
    
    if rootNode.left is not None and rootNode.left.value >  rootNode.value: 
        return False
    
    if rootNode.left is not None and checkHelper(rootNode.left, rootNode.value, 'left') is False:
        return False
    if rootNode.right is not None and checkHelper(rootNode.right, rootNode.value, 'right') is False:
        return False
    
    if checkIfBSTIsBalanced(rootNode.right) is False or checkIfBSTIsBalanced(rootNode.left) is False:
        return False
    
    return True

if __name__ == '__main__':
    root = Node(5)

    #right subtree
    root.right = Node(10)
    root.right.left = Node(6)
    #root.right.left.right = Node(20)

    #left subtree
    root.left = Node(3)
    root.left.right = Node(4)

    printTree(root)

    print(checkIfBSTIsBalanced(root))
