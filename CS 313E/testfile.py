def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                print("List is:", alist)
                print("Swapping", alist[i], "with", alist[i+1])
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                dummy = input("")
        print("End of pass:", alist, "\n")

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)- 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                print("List is:", alist)
                print("Swapping", alist[i], "with", alist[i+1])
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                dummy = input("")
        passnum -= 1
        print("End of pass:", alist, "\n")

def selectionSort(alist):
    count = 0
    print("Original list:", alist)
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                print("New max is", alist[location])
                positionOfMax = location
                count += 1
        print("Swapping", alist[positionOfMax], "with", alist[fillslot])
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
        print("End of pass:", alist, "\n")
    print(count)

def insertionSort(alist):
    count = 0
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        print("List is", alist)
        print("Sorted portion:", alist[:index])
        position = index
    
        while position>0 and alist[position-1]>currentvalue:
            count += 1
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue
        print("List is now:", alist, "\n")
    print(count)


def main():

    alist = [1,2,3,4,5,6,7,8]
    bubbleSort(alist)

main()
