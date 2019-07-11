#  File: LinkedLists.py
#  Description: Methods for Linked Lists

class Node:

    def __init__(self, initdata):       #Node
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        string = ""
        current = self.head
        count = 1
        while (current != None):            #iterates through list
            if (count != 0 and count % 10 == 0):            #if 10 has been printed, print a new line
                string = string + str(current.getData()).ljust(6) + "\n"
                current = current.getNext()
                count += 1
            else:                           #print with 2 spaces in between
                string = string + str(current.getData()).ljust(6) + "  "
                current = current.getNext()
                count += 1
        string = string + "\n"
        return string

    def addFirst(self, item):
        temp = Node(item)
        temp.setNext(self.head)     #item is added to the front
        self.head = temp

    def addLast(self, item):
        temp = Node(item)
        previous = None
        current = self.head
        if (current == None):       #if there is nothing in the list yet
            self.head = temp
        else:
            while (current != None):    #iterates through and sets the last node pointing to temp
                previous = current
                current = current.getNext()
            previous.setNext(temp)

    def addInOrder(self, item):
        current = self.head
        previous = None
        tooBig = False

        while (current != None and not tooBig):     #iterates through and stops once the item is better than what it is compared to
            if (current.getData() > item):
                tooBig = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if (previous == None):          #if there is only one element, set the head to the item
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)       #set the previous pointer to the temp and temp pointing to the current
            previous.setNext(temp)

    def getLength(self):
        count = 0
        current = self.head

        while (current != None):        #iterates through and counts how many nodes there are
            count += 1
            current = current.getNext()

        return count

    def findUnordered(self, item):
        current = self.head
        found = False

        while (current != None and not found):      #iterates through
            if (current.getData() == item):         #if match, then found is true and gets out of loop
                found = True
            else:
                current = current.getNext()

        return found

    def findOrdered(self, item):
        current = self.head
        found = False
        tooBig = False

        while (current != None and not found and not tooBig):       #iterates through until either it hits the end, or the item is bigger than current
            if (current.getData() == item):                 #if match, then found is true and gets out of loop
                found = True
            else:
                if (current.getData() > item):              #once current is bigger than item, then there is no way item will be in the list
                    tooBig = True
                else:
                    current = current.getNext()

        return found

    def delete(self, item):
        current = self.head
        previous = None
        found = False

        while (current != None and not found):              #iterates through list
            if (current.getData() == item):                 #if it found the item,
                if (current.getNext() == None and previous != None):    #if it is the last item
                    previous.setNext(None)
                    found = True
                elif (previous == None):                                #if it is the first item
                    self.head = current.getNext()
                    found = True
                else:                                                   #if its in the middle
                    previous.setNext(current.getNext())
                    found = True
            else:
                previous = current
                current = current.getNext()                 #iterate

        return found

    def copyList(self):
        newList = LinkedList()
        current = self.head

        while (current != None):
            newList.addLast(current.getData())          #iterates through original list and creates another list that is in the same order
            current = current.getNext()

        return newList

    def reverseList(self):
        newList = LinkedList()
        current = self.head

        while (current != None):
            newList.addFirst(current.getData())         #iterates through original list and creates another list that is in the opposite order
            current = current.getNext()

        return newList

    def orderList(self):
        originalList = self.copyList()
        newList = LinkedList()
        count = originalList.getLength()                #needs length for a loop controller

        while (count > 0):
            current = originalList.head
            smallest = current
            while (current != None):                    #iterates through
                if (current.getData() < smallest.getData()):        #if current is less than smaller, then the smaller becomes the current
                    smallest = current
                current = current.getNext()
            newList.addLast(smallest.getData())                     #adds smallest to new list, and deletes smallest from the orginal list
            originalList.delete(smallest.getData())
            count -= 1                                              #subtracts 1 from count because deleted an item
            
        return newList

    def isOrdered(self):
        current = self.head
        ordered = True

        while (current != None and current.getNext() != None and ordered):
            if (current.getData() < current.getNext().getData()):               #if the previous node is less than the current, then keep iterate
                current = current.getNext()
            else:
                ordered = False                                                 #otherwise, it's not in order

        return ordered

    def isEmpty(self):
        return self.head == None                #a list is empty if the head is None

    def mergeList(self, b):
        newList = b
        current = self.head
        
        while (current != None):
            newList.addLast(current.getData())          #add the fist list's elements to the second list
            current = current.getNext()

        newList = newList.orderList()               #order the list and return it
        return newList
    
    def isEqual(self, b):
        list1current = self.head
        list2current = b.head
        equal = True
        if (self.getLength() != b.getLength()):             #if the two lists do not have the same number of elements, they cannot be equal
            equal = False

        while (list1current != None and list2current != None and equal):
            if (list1current.getData() == list2current.getData()):
                list1current = list1current.getNext()               #checks to see if each element are the same, if not, then they are not equal
                list2current = list2current.getNext()
            else:
                equal = False

        return equal

    def removeDuplicates(self):
        newList = self
        current = newList.head

        while (current != None):
            previous = None
            item = current.getNext()
            while(item != None):                            #iterates through each Node checking to see if there are duplicates
                if (item.getData() == current.getData()):
                    if (previous == None):                  #if first item is a duplicate, set the head to the pointer after the current
                        current.setNext(item.getNext())
                    else:
                        previous.setNext(item.getNext())    #otherwise, set the previous pointer to the next node after the dupliate
                previous = item
                item = item.getNext()
            current = current.getNext()                     #iterates through

        return newList
    

# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
