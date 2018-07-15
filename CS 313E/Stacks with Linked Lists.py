class Stack (object):
   def __init__(self):
       self.head = None

   def isEmpty(self):
      return self.head == None

   def push(self, item):
      temp = Node(item)
      temp.setNext(self.head)
      self.head = temp

   def pop(self):
      item = self.head.getData()
      self.head.setNext(self.head.getNext())
      return item

   def peek(self):
      return self.items [len(self.items)-1]

   def size(self):
      return len(self.items)

   def __str__(self):
      outString = ""
      current = self.head
      while (current != None):
         outString = outString + current.getData() + " "
         current = current.getNext()
      return outString
