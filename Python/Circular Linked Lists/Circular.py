#  File: Circular.py
#  Description: HotPotato game with circular lists

class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this â€“ saves a lot
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER

class CircularList(object):

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)                 #sets item to a node
        current = self.head
        
        if (current == None):             #if there is nothing in the list, set head to temp and set temp's next to itself
            self.head = temp
            self.head.setNext(self.head)
        elif (current.getNext() == self.head):     #if there is one node in the list, set the head's next to temp and temp's next to the first item
            temp.setNext(self.head)
            self.head.setNext(temp)
        else:                                         #otherwise, counts to the end of the list, sets the temp's next to the head
            while (current.getNext() != self.head):   #and the last node's next to the node to be added
                current = current.getNext()
            temp.setNext(self.head)
            current.setNext(temp)

    def isEmpty(self):
        return self.head == None             #if head is pointed to None, there is nothing in the list

    def onlyOneNode(self):
        return self.head.getNext() == self.head             #if the head is pointing to itself, there is only one node

    def remove(self, current, previous):

        nextNode = current.getNext()               #sets the node to be returned the node after the node to be deleted
        if (self.head == current):                 #if the node to be removed is the first node in the list
            self.head = nextNode                   #sets head to the node after the node to be removed
            previous.setNext(self.head)            #the last node's next is set to the head
        else:
            previous.setNext(nextNode)             #otherwise, just set the previous node's next to the node after the node to be removed

        return nextNode                            #returns the node after current

    def __str__(self):
        string = ""
        current = self.head
        count = 1
        while (current.getNext() != self.head):       #counts how many items are in the list
            count += 1
            current = current.getNext()
        current = self.head
        for i in range(1,count+1):
            if (i % 10 == 0 and i != 0):                             #if the item printed is the tenth one on a line, print item with a new line
                string = string + " " + current.getData() + "\n"
                current = current.getNext()
            else:                                                    #otherwise, just print item with a space after
                string = string + " " + current.getData() + " "
                current = current.getNext()
        return string

def hotPotato(theList, iterations):

    cList = theList                                   #creates a circular list to be manipulated
    previous = None
    current = cList.head
    iteration = 1
    while (not cList.onlyOneNode()):                  #while there is at least 2 nodes, iterates to the nth person, and removes the nth person from the list
        for i in (range(iterations-1)):
            previous = current
            current = current.getNext()
        print("Iteration", iteration)
        print(current.getData(), "was deleted")
        nextNode = cList.remove(current, previous)
        print(cList, "\n")
        current = nextNode
        iteration += 1

def main():

    file = open("HotPotatoData.txt", "r")
    fString = file.readline()                         #reads in a line initially
    while (fString != ""):                            #while the thing that is read in is not at the end of the file
       cList = CircularList()
       numPeople = 0
       iterations = 0
       header = fString.split()
       numPeople = int(header[0])                     #sets the first number to the number of people
       iterations = int(header[1])                    #sets the second number to the number of iterations to count through
       for i in range(numPeople):                     #for n players, reads in n lines for each name
           player = file.readline()
           player = player.rstrip("\n")
           cList.add(player)
       print("Number of numPeople:", numPeople)
       print(cList,"\n")
       hotPotato(cList, iterations)                   #does the hot potato game for each dataset
       print("The sole survivor is:", cList, "\n\n")
       fString = file.readline()                      #reads in the next line
        
main()
