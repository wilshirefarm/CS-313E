class Node:

    def __init__(self, initdata):
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

class OrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0

        while (current != None):
            count += 1
            current = current.getNext()

        return count

    def remove(self, item):

        current = self.head
        previous = None
        found = False

        while(not found):
            if (item == current.getData()):
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if (previous == None):
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def add(self, item):
        current = self.head
        previous = None
        found = False

        while (current != None and not found):
            if (current.getData() > item):
                found = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if (previous == None):
            temp.setNext(current)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)







        
    
