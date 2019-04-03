def iAddition(self):

    total = 0
    
    while (current != None):

        total = total + current.getData()
        current = current.getNext()

    return total

def rAddition(listPtr):

    if listPtr == None:
        return 0
    else:
        return listPtr + rAddition(listPtr.getNext())
