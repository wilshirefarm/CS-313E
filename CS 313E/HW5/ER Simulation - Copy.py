#  File: ER Simulation.py
#  Description: Simulates an ER room with queues
#  Student's Name: Wilshire Liu
#  Student's UT EID: WL7583
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 10/13/16
#  Date Last Modified: 10/13/16

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

def main():

    file = open("ERsim.txt", "r")   #opens file
    Critical = Queue()              #creates the 3 queues
    Serious = Queue()
    Fair = Queue()
    
    lines = 0
    for l in file:      #counts number of lines in the text file
        lines += 1
    file.seek(0)        #sets the cursor back to the beginning

    for i in range(lines):      #loops through each line
        command = file.readline()
        command = command.split()
        if (command[0] == "add"):       #if it's an add command
            patient = command[1]
            print(">>> Add patient " + patient + " to " + command[2] + " queue\n")
            if (command[2] == "Critical"):
                Critical.enqueue(patient)       #if command says Critical, add to Critical queue
            elif (command[2] == "Serious"):
                Serious.enqueue(patient)        #else if command says Serious, add to Serious queue
            elif (command[2] == "Fair"):
                Fair.enqueue(patient)           #else if command says Fair, add to Fair queue
            print("   Queues are:\n   Critical:", Critical, "\n   Serious: ", Serious, "\n   Fair:    ", Fair, "\n")    #prints out the queues
        elif (command[0] == "treat"):       #if it's a treat command
            if (command[1] == "next"):      #treat next command
                print(">>> Treat next patient\n")
                if (not Critical.isEmpty()):        #if Critical queue is not empty, treat the next Critical patient
                    print("   Treating '" + str(Critical.dequeue()) + "' from Critical queue")
                    print("   Queues are:\n   Critical:", Critical, "\n   Serious: ", Serious, "\n   Fair:    ", Fair, "\n")
                elif (not Serious.isEmpty()):       #else if Serious queue is not empty, treat the next Serious patient
                    print("   Treating '" + str(Serious.dequeue()) + "' from Serious queue")
                    print("   Queues are:\n   Critical:", Critical, "\n   Serious: ", Serious, "\n   Fair:    ", Fair, "\n")
                elif (not Fair.isEmpty()):          #else if Fair queue is not empty, treat the next Fair patient
                    print("   Treating '" + str(Fair.dequeue()) + "' from Fair queue")
                    print("   Queues are:\n   Critical:", Critical, "\n   Serious: ", Serious, "\n   Fair:    ", Fair, "\n")
                else:                               #if all queues are empty prints no more patients left
                    print("   No patients in queues\n")
            elif (command[1] == "all"):     #treat all command
                print(">>> Treat all patients\n")
                while (not Critical.isEmpty()):     #loops through Critical queue first
                    print("   Treating '" + str(Critical.dequeue()) + "' from Critical queue")
                    print("   Queues are:\n   Critical:", Critical, "\n   Serious: ", Serious, "\n   Fair:    ", Fair, "\n")
                while (not Serious.isEmpty()):      #loops through Serious queue next
                    print("   Treating '" + str(Serious.dequeue()) + "' from Serious queue")
                    print("   Queues are:\n   Critical:", Critical, "\n   Serious: ", Serious, "\n   Fair:    ", Fair, "\n")
                while (not Fair.isEmpty()):         #loops through Fair queue last
                    print("   Treating '" + str(Fair.dequeue()) + "' from Fair queue")
                    print("   Queues are:\n   Critical:", Critical, "\n   Serious: ", Serious, "\n   Fair:    ", Fair, "\n")
                print("   No patients in queues\n")     #after all patients treated, prints no more patients left
            else:                           #if it's a specific treat condition command
                if (command[1] == "Critical"):
                    print(">>> Treat next patient on Critical queue\n")         #treats Critical queue
                    print("   Treating '" + str(Critical.dequeue()) + "' from the Critical queue")
                elif (command[1] == "Serious"):
                    print(">>> Treat next patient on Serious queue\n")          #treats Serious queue
                    print("   Treating '" + str(Serious.dequeue()) + "' from the Serious queue")
                elif (command[1] == "Fair"):
                    print(">>> Treat next patient on Fair queue\n")             #treats Fair queue
                    print("   Treating '" + str(Fair.dequeue()) + "' from the Fair queue")
                print("   Queues are:\n   Critical:", Critical, "\n   Serious: ", Serious, "\n   Fair:    ", Fair, "\n")    #prints out the queues
        else:
            print(">>> Exit\n")         #if command is exit, print "Exit"

main()
