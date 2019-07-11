#  File: Sorting.py
#  Description: Displays the average times of the 6 sorting methods with 10, 100, and 1000 elements when the lists are randomized, sorted, reversed, and almost sorted

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def main():

#Random Lists
    
    print("Input type = Random")
    bubbleSortLine = ("bubbleSort").rjust(16) + "    "
    selectionSortLine = ("selectionSort").rjust(16) + "    "
    insertionSortLine = ("insertionSort").rjust(16) + "    "
    shellSortLine = ("shellSort").rjust(16) + "    "                    #formats the lines for each search's time outputs
    mergeSortLine = ("mergeSort").rjust(16) + "    "
    quickSortLine = ("quickSort").rjust(16) + "    "
    
    integers = [10, 100, 1000]                          #makes a list of integers 10, 100, and 1000
    for i in integers:                                  #loops through each set of n
        times = []                                      #creates a list for the 5 runtimes
        for f in range(5):                              #runs the test 5 times
            myList = [i for i in range(i)]              #makes a list from 0 to n
            random.shuffle(myList)                      #shuffles list
            startTime = time.perf_counter()
            bubbleSort(myList)                          #bubbleSort
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)                   #adds the time to the times list
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5                     #finds the average time by dividing the times by 5
        bubbleSortLine = bubbleSortLine + "{:8.6f}".format(averageTime).ljust(11)       #outputs the time
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            selectionSort(myList)                       #does the same for selectionSort
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        selectionSortLine = selectionSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            insertionSort(myList)                       #does the same for insertionSort
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        insertionSortLine = insertionSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            shellSort(myList)                           #does the same for shellSort
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        shellSortLine = shellSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            mergeSort(myList)                           #does the same for mergeSort
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        mergeSortLine = mergeSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            random.shuffle(myList)
            startTime = time.perf_counter()
            quickSort(myList)                           #does the same for quickSort
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        quickSortLine = quickSortLine + "{:8.6f}".format(averageTime).ljust(11)
        
    print("                    avg time   avg time   avg time")
    print(("Sort function").rjust(16) + "     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print(bubbleSortLine)
    print(selectionSortLine)
    print(insertionSortLine)
    print(shellSortLine)
    print(mergeSortLine)
    print(quickSortLine)
    print("\n")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Sorted Lists  
##################################################################################################
# Same documentation as the previous section except does not shuffle and keeps the list as it is #
##################################################################################################

    print("Input type = Sorted")
    bubbleSortLine = ("bubbleSort").rjust(16) + "    "
    selectionSortLine = ("selectionSort").rjust(16) + "    "
    insertionSortLine = ("insertionSort").rjust(16) + "    "
    shellSortLine = ("shellSort").rjust(16) + "    "
    mergeSortLine = ("mergeSort").rjust(16) + "    "
    quickSortLine = ("quickSort").rjust(16) + "    "
    
    integers = [10, 100, 1000]
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        bubbleSortLine = bubbleSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        selectionSortLine = selectionSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        insertionSortLine = insertionSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        shellSortLine = shellSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        mergeSortLine = mergeSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        quickSortLine = quickSortLine + "{:8.6f}".format(averageTime).ljust(11)
        
    print("                    avg time   avg time   avg time")
    print(("Sort function").rjust(16) + "     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print(bubbleSortLine)
    print(selectionSortLine)
    print(insertionSortLine)
    print(shellSortLine)
    print(mergeSortLine)
    print(quickSortLine)
    print("\n")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Reversed Lists
#######################################################################
# Same documentation as the previous section except reverses the list #
#######################################################################

    print("Input type = Reverse")
    bubbleSortLine = ("bubbleSort").rjust(16) + "    "
    selectionSortLine = ("selectionSort").rjust(16) + "    "
    insertionSortLine = ("insertionSort").rjust(16) + "    "
    shellSortLine = ("shellSort").rjust(16) + "    "
    mergeSortLine = ("mergeSort").rjust(16) + "    "
    quickSortLine = ("quickSort").rjust(16) + "    "
    
    integers = [10, 100, 1000]
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            myList.reverse()                                #reverses list
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        bubbleSortLine = bubbleSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            myList.reverse()                                #reverses list
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        selectionSortLine = selectionSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            myList.reverse()                                #reverses list
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        insertionSortLine = insertionSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            myList.reverse()                                #reverses list
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        shellSortLine = shellSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            myList.reverse()                                #reverses list
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        mergeSortLine = mergeSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            myList.reverse()                                #reverses list
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        quickSortLine = quickSortLine + "{:8.6f}".format(averageTime).ljust(11)
        
    print("                    avg time   avg time   avg time")
    print(("Sort function").rjust(16) + "     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print(bubbleSortLine)
    print(selectionSortLine)
    print(insertionSortLine)
    print(shellSortLine)
    print(mergeSortLine)
    print(quickSortLine)
    print("\n")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Almost Sorted Lists
##########################################################################################
# Same documentation as the previous section except swaps 10% of the numbers in the list #
##########################################################################################

    print("Input type = Almost Sorted")
    bubbleSortLine = ("bubbleSort").rjust(16) + "    "
    selectionSortLine = ("selectionSort").rjust(16) + "    "
    insertionSortLine = ("insertionSort").rjust(16) + "    "
    shellSortLine = ("shellSort").rjust(16) + "    "
    mergeSortLine = ("mergeSort").rjust(16) + "    "
    quickSortLine = ("quickSort").rjust(16) + "    "
    
    integers = [10, 100, 1000]
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            for s in range(int(i/10)):                                  #loops through 10% of the length of the list
                randomIndex = random.randint(0,len(myList)-1)           #finds first random place to swap
                randomIndex2 = random.randint(0,len(myList)-1)          #finds second random place to swap
                myList[randomIndex] = randomIndex2                      #does the swaping
                myList[randomIndex2] = randomIndex
            bubbleSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        bubbleSortLine = bubbleSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            for s in range(int(i/10)):                                  #loops through 10% of the length of the list
                randomIndex = random.randint(0,len(myList)-1)           #finds first random place to swap
                randomIndex2 = random.randint(0,len(myList)-1)          #finds second random place to swap
                myList[randomIndex] = randomIndex2                      #does the swaping
                myList[randomIndex2] = randomIndex
            selectionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        selectionSortLine = selectionSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            for s in range(int(i/10)):                                  #loops through 10% of the length of the list
                randomIndex = random.randint(0,len(myList)-1)           #finds first random place to swap
                randomIndex2 = random.randint(0,len(myList)-1)          #finds second random place to swap
                myList[randomIndex] = randomIndex2                      #does the swaping
                myList[randomIndex2] = randomIndex
            insertionSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        insertionSortLine = insertionSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            for s in range(int(i/10)):                                  #loops through 10% of the length of the list
                randomIndex = random.randint(0,len(myList)-1)           #finds first random place to swap
                randomIndex2 = random.randint(0,len(myList)-1)          #finds second random place to swap
                myList[randomIndex] = randomIndex2                      #does the swaping
                myList[randomIndex2] = randomIndex
            shellSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        shellSortLine = shellSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            for s in range(int(i/10)):                                  #loops through 10% of the length of the list
                randomIndex = random.randint(0,len(myList)-1)           #finds first random place to swap
                randomIndex2 = random.randint(0,len(myList)-1)          #finds second random place to swap
                myList[randomIndex] = randomIndex2                      #does the swaping
                myList[randomIndex2] = randomIndex
            mergeSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        mergeSortLine = mergeSortLine + "{:8.6f}".format(averageTime).ljust(11)
    for i in integers:
        times = []
        for f in range(5):
            myList = [i for i in range(i)]
            startTime = time.perf_counter()
            for s in range(int(i/10)):                                  #loops through 10% of the length of the list
                randomIndex = random.randint(0,len(myList)-1)           #finds first random place to swap
                randomIndex2 = random.randint(0,len(myList)-1)          #finds second random place to swap
                myList[randomIndex] = randomIndex2                      #does the swaping
                myList[randomIndex2] = randomIndex
            quickSort(myList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            times.append(elapsedTime)
        totalTime = 0
        for t in times:
            totalTime = totalTime + t
        averageTime = totalTime / 5
        quickSortLine = quickSortLine + "{:8.6f}".format(averageTime).ljust(11)
        
    print("                    avg time   avg time   avg time")
    print(("Sort function").rjust(16) + "     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print(bubbleSortLine)
    print(selectionSortLine)
    print(insertionSortLine)
    print(shellSortLine)
    print(mergeSortLine)
    print(quickSortLine)
    print("\n")

main()
