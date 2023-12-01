# Python program to insert a node
# in a BST
  
# Given Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
  
# Function to insert a new node with
# given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
  
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
  
    # Return the node pointer
    return node

# Function to do preorder traversal of BST
def preOrder(root):
    if root is not None:
        print(root.key, end=" ")
        preOrder(root.left)
        preOrder(root.right)
  
# Driver Code
if __name__ == '__main__':
    """ Let us create following BST
          50
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
    preOrder(root)

""" # Python3 program to convert a left
# unbalanced BST to a balanced BST
import sys
import math
 
# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
 
# This function traverse the skewed binary tree and
# stores its nodes pointers in vector nodes[]
def storeBSTNodes(root,nodes):
     
    # Base case
    if not root:
        return
     
    # Store nodes in Inorder (which is sorted
    # order for BST)
    storeBSTNodes(root.left,nodes)
    nodes.append(root)
    storeBSTNodes(root.right,nodes)
 
# Recursive function to construct binary tree
def buildTreeUtil(nodes,start,end):
     
    # base case
    if start>end:
        return None
 
    # Get the middle element and make it root
    mid=(start+end)//2
    node=nodes[mid]
 
    # Using index in Inorder traversal, construct
    # left and right subtress
    node.left=buildTreeUtil(nodes,start,mid-1)
    node.right=buildTreeUtil(nodes,mid+1,end)
    return node
 
# This functions converts an unbalanced BST to
# a balanced BST
def buildTree(root):
     
    # Store nodes of given BST in sorted order
    nodes=[]
    storeBSTNodes(root,nodes)
 
    # Constructs BST from nodes[]
    n=len(nodes)
    return buildTreeUtil(nodes,0,n-1)
 
# Function to do preorder traversal of tree
def preOrder(root):
    if not root:
        return
    print("{} ".format(root.data),end="")
    preOrder(root.left)
    preOrder(root.right)
 
# Driver code
if __name__=='__main__':
    # Constructed skewed binary tree is
    #         10
    #         /
    #         8
    #         /
    #     7
    #     /
    #     6
    #     /
    # 5
    root = Node(30)
    root.left = Node(20)
    root.left.left = Node(10)
    #root.left.left.left = Node(6)
    #root.left.left.left.left = Node(5)
    root = buildTree(root)
    print("Preorder traversal of balanced BST is :")
    preOrder(root) """