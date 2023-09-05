class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    #get the top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is emty')
        return self.head.next.value

    #push a value into the stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    #remove a value
    def pop(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
    

#Driver code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)    
    print(f"Stack: {stack}")
    

    for _ in range(1,6):
        remove = stack.pop()
        #print(f"Pop: {remove}")
    print(f"Stack: {stack}")
