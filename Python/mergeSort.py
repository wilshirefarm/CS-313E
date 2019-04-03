def mergeSort(alist):

    print("Sorting:", alist)
    dummy = input("")

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        print("Recursive call on the left half:", lefthalf)
        mergeSort(lefthalf)
        print("Recursive call on the right half:", righthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        print("Merging", lefthalf, "and", righthalf)
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

        print("Sorted list:", alist)
        dummy = input("")

def main():

   board = [1, 4, 7, 2, 3, 9, 6, 8, 5]
   mergeSort(board)
   print(board)

main()
