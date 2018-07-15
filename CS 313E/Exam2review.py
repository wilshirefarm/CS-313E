class Stack:
   def __init__(self):
      self.items = []

   def isEmpty(self):
      return self.items == []

   def push(self, item):
      self.items.append(item)

   def pop(self):
      return self.items.pop()

   def peek(self):
      return self.items[len(self.items)-1]

   def size(self):
      return len(self.items)

   def __str__(self):
      return str(self.items)

   def addStack(self):
      total = 0
      if self.isEmpty():
         return 0
      else:
         item = self.pop()
         total = item + self.addStack()
         self.push(item)
         return total

class Queue:

   def __init__(self):
      self.items = []

   def enqueue(self, item):
      self.items.append(item)

   def dequeue(self):
      return self.items.pop(0)

   def isEmpty(self):
      return self.items == []

   def size(self):
      return len(self.items)

   def peek(self):
      return self.items[0]

   def __str__(self):
      return str(self.items)

   def addQueue(self):
      total = 0
      if not self.isEmpty():
         item = self.dequeue()
         total = item + self.addQueue()
         self.enqueue(item)
      return total
   #but this will print queue backwards
        
def main():

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.addStack())
    print(stack)

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.addQueue())
    print(queue)

main()

