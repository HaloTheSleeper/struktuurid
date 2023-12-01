class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class dl_list:
    def __init__(self):
        self.head = None
    
    #push element
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    #insert node after given node
    def insert(self, prev_node, newVal):
        if prev_node is None:
            return
        newNode = Node(newVal)
        newNode.next = prev_node.next
        prev_node.next = newNode
        newNode.prev = prev_node
        if newNode.next is not None:
            newNode.next.prev = newNode
    
    #append a item to the end of the list
    def append(self, data):
        newNode = Node(data)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        newNode.prev = last
        last.next = newNode
        return

    def printList(self):
        print('#########')
        node = self.head
        while (node is not None):
            print(node.data)
            node = node.next
    

list = dl_list()
list.push(1)
list.push(2)
list.push(3)
list.insert(list.head.next, 10)
list.append(20)
list.printList()