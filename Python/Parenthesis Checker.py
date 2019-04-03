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

   def __str__ (self):
      return str(self.items)

    
def parChecker (symbolString):

   s = Stack()
   balanced = True
   index = 0
   print("Testing string ",symbolString)

   while index < len(symbolString) and balanced:

      symbol = symbolString[index]

      print("symbol:",symbol)
      if symbol in "([{":
         s.push (symbol)
         print("   pushed: stack now ",str(s))
         input("paused")
      else:
         # there had better be a matching open paren on the stack
         if s.isEmpty():
            balanced = False
            print("   Stack is empty! Aborting")
            input("paused")
         else:
            top = s.pop()
            if not matches (top,symbol):
               balanced = False
               print("   Mismatch found! Aborting")
               input("paused")
            else:
               print("   Match found: stack after pop now: ",str(s))
               input("paused")

      index += 1

   # while loop is over
   if balanced and s.isEmpty():
      return True
   else:
      return False


def matches (open, close):
   opens = "([{"
   closes = ")]}"

   return opens.index(open) == closes.index(close)


def main():

    example1 = "()[()]"
    print (example1,":"," matches\n\n" if parChecker(example1) else " does not match\n\n")
    example2 = "([])({})"
    print (example2,":"," matches\n\n" if parChecker(example2) else " does not match\n\n")
    example3 = "{]()"
    print (example3,":"," matches\n\n" if parChecker(example3) else " does not match\n\n")

main()
