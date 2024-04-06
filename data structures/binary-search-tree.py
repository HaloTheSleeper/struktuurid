class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
  
def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
  
    return node

def xOrder(root):
    if root is not None:
        xOrder(root.left)
        xOrder(root.right)
        print(root.key, end=" ")
if __name__ == '__main__':
    """   50
       /     \
      30      70
     /  \    /  \
    20  40  60   80 """
    
    root = None
  
    root = None
    keys = [50, 70, 30, 20, 40, 60, 80]
  
    # Creating the BST
    for key in keys:
        root = insert(root, key)
  
    # Function Call
    xOrder(root)

