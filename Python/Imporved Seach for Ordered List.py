def search(self, item):

    current = self.head
    found = False
    tooBig = False

    while (current != None and not found and not tooBig):
        if current.getData() == item:
            found = True
        else:
            if current.getData() > item:
                tooBig = True
            else:
                current = current.getNext()

    return found
