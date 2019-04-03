class Stack (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items [len(self.items)-1]

   def size (self):
      return len(self.items)

##################################################

def main():

   print("Running Stack1.py")
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
