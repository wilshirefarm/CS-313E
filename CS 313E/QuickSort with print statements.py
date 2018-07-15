def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        print("recursive call: sort left sublist from",alist[first],"to",alist[splitpoint-1])
        quickSortHelper(alist,first,splitpoint-1)
        print("recursive call: sort right sublist from",alist[splitpoint+1],"to",alist[last])
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]
    print("pivot =",pivotvalue)
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        print("   item bigger than pivot:",alist[leftmark],", item smaller than pivot:",alist[rightmark])
        if rightmark < leftmark:
            print("   crossover:  done with pass")
            done = True
        else:
            print("   swapping",alist[leftmark],"and",alist[rightmark])
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            print("   list now: ",alist)
            dummy=input("")

    print("   moving pivot: swapping",alist[first],"and",alist[rightmark])
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    print("   list now: ",alist)
    dummy=input("")

    return rightmark


def main():
    
    myList = [54,26,93,17,77,31,44,55,20]

    print("Initial list: ", myList)
    quickSort(myList)
    print("Final list: ",myList)

main()
