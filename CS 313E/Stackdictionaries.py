class Stack ():
    def __init__(self):
       self.items = { }
       self.top = 0

    def isEmpty (self):
        return self.top == 0

    def push (self, item):
        self.top += 1
        self.items[self.top] = item

    def pop (self):
        item = self.items[self.top]
        self.top -= 1
        return item

    def peek (self):
        return self.items[self.top]

    def size (self):
        return self.top

##################################################

def main():

    print("Running Stack2.py")
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
