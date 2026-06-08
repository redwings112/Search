class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node = Node(value)
            if self.head:
                new_node.next = self.head
            self.head = new_node
            self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def stackSize(self):
        return self.size

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()

myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traversAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())

