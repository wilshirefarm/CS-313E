class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def deqeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]
