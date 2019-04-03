import random

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]


def hotPotato(namelist,num):

   simqueue = Queue()

   for name in namelist:
      simqueue.enqueue(name)

   while simqueue.size() > 1:
      for i in range(num-1):
         simqueue.enqueue(simqueue.dequeue())

      print("Deleting",simqueue.peek())
      pause = input("pausing. . .")
      simqueue.dequeue()

   return simqueue.dequeue()


def main():

   survivors = ["P1,"P2","P3","P4","P5","P6"]

   random.shuffle(survivors)
   print(survivors)

   pause = input("pausing. . .")
   survivor = hotPotato(survivors, 7)
   print("Survivor is: ",survivor)

main()
