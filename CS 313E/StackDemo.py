class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def main():

    myStack = Stack()
    print(myStack.isEmpty())
    myStack.push("cat")
    myStack.push(4)
    print(myStack.peek())
    myStack.push(False)
    print(myStack.size())
    print(myStack.isEmpty())
    myStack.push(98.6)
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.size())
    
main()
