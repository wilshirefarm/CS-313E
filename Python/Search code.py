#
#  Basic sequential search
#
def sequentialSearch(alist,item):
   pos = 0
   found = false

   while pos < len(alist) and not found:
      if alist[pos] == item:
         found = True
      else:
         pos = pos + 1

   return(found)

#
#  Sequential search of an ordered list
#
def orderedSequentialSearch(alist,item):
   pos = 0
   found = false
   stop = false

   while pos < len(alist) and not found and not stop:
      if alist[pos] == item:
         found = True
      else:
         if alist[pos] > item:
            stop = True
         else:
            pos = pos + 1

   return(found)

#
#  Basic (iterative) binary search
#  the list MUST be ordered for binary search!
#
def binarySearch(alist,item):
    
    first = 0
    last = len(alist)-1
    found = false

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return(found)
   
#
#  Recursive version of binary search
#  the list MUST be ordered for binary search!
#
def rBinarySearch(alist,item):
    if len(alist) == 0:
        return(False)
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return(True)
        else:
            if item < alist[midpoint]:
                return rBinarySearch(alist[:midpoint],item)
            else:
                return rBinarySearch(alist[midpoint+1:],item)
