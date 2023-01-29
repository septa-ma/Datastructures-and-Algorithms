# what is sorting?
# A Sorting Algorithm is used to rearrange a given array or list of elements 
# according to a comparison operator on the elements.
# popular sort algorithms:
# 1- selection sort:
# sorts an array by repeatedly finding the minimum element from the unsorted 
# part and putting it at the beginning. 
# steps to solve the problem:
# - Initialize minimum value(min_idx) to location 0.
# - Traverse the array to find the minimum element in the array.
# - While traversing if any element smaller than min_idx is found then swap both the values.
# - Then, increment min_idx to point to the next element.
# - Repeat until the array is sorted.
# 2- insertion sort:
# works similar to the way you sort playing cards in your hands. 
# virtually split into a sorted and an unsorted part. Values from the unsorted
# part are picked and placed at the correct position in the sorted part.
# steps to solve the problem:
# - compare the first two elements and sort them.
# - pick the third element and find its proper position among the previous 
# two sorted elements till the end.
# 3- quick sort:
# it picks an element as a pivot and partitions the given array around the pivot. 
# we can pick pivot in different ways:
# - pick the first element.
# - pick the last element.
# - pick a random element.
# - pick median.
# 4- merge sort:
# dividing an array into smaller subarrays, sorting each subarray, and then 
# merging the sorted subarrays back together to form the final sorted array.
# 5- bubble sort:
# repeatedly swapping the adjacent elements if they are in the wrong order. 
# it is not suitable for large data sets.

# 1- selection sort
def selectionSort(myList):
    for i in range(len(myList)):
        minId = i
        for j in range(i+1, len(myList)):
            if(myList[minId] > myList[j]):
                minId = j
        # swap greater element with smaller one
        myList[i], myList[minId] = myList[minId], myList[i]

myList1 = [32,85,4,69,10,78,5,15,30,17,9,41,13,20,11,54]
selectionSort(myList1)
print("1- selection sort of my list is: ",myList1)

# 2- insertion sort
def insertionSort(myList):
    for i in range(1, len(myList)):
        j = i - 1
        nextValue = myList[i]
        while myList[j] > nextValue and j >= 0:
            myList[j+1] = myList[j]
            j -= 1
        myList[j+1] = nextValue

myList2 = [22,85,48,609,10,8,5,15,30,17,9,41,13,20,110,514]
insertionSort(myList2)
print("2- insertion sort of my list is: ",myList2)

# 3- quick sort use divide and conquer approach
def quickSort(myList, start, end):
    if start >= end:
        return myList
    # find the pivot
    p = pivot(myList, start, end)
    # sort each sub-list recursively
    quickSort(myList, start, p-1)
    quickSort(myList, p+1, end)

# pick the first element as a pivot.
def pivot(myList, start, end):
    pivot = myList[start]
    low = start + 1
    high = end
    while True:
        # moving to left from end
        while low <= high and myList[high] >= pivot:
            high -= 1
        # moving to right from start
        while low <= high and myList[low] <= pivot:
            low += 1
        # if low < high swap values else break cause find the pivot
        if low <= high:
            myList[low], myList[high] = myList[high], myList[low]
        else:
            break
    # put the pivot value in the correct position
    myList[start], myList[high] = myList[high], myList[start]
    return high

myList3 = [22,85,48,69,10,17,9,41,13,1,20,54,3]
quickSort(myList3, 0, len(myList3)-1)
print("3- quick sort of my list is: ",myList3)

# 4- merge sort use divide and conquer approach
def mergeSort(myList):
    if len(myList) <= 1:
      return myList
    # find middle of the list and make left and right sub-list
    mid = len(myList)//2
    leftList = myList[:mid]
    rightList = myList[mid:]
    # do the above calculation for each half recursively
    leftList = mergeSort(leftList)
    rightList = mergeSort(rightList)
    return list(merge(leftList, rightList))

def merge(leftList, rightList):
    sortedList = []
    # comparing elements in each half
    while len(leftList) != 0 and len(rightList) != 0:
        if leftList[0] < rightList[0]:
            sortedList.append(leftList[0])
            leftList.remove(leftList[0])
        else:
            sortedList.append(rightList[0])
            rightList.remove(rightList[0])
    # merging 2 halves
    if len(leftList) == 0:
        sortedList = sortedList + rightList
    else:
        sortedList = sortedList + leftList
    # return sorted list
    return sortedList

myList4 = [22,85,48,609,10,8,9,10,41,13,20,110,514]
print("4- merge sort of my list is: ",mergeSort(myList4))

# 5- bubble sort
def bubbleSort(myList):
    for i in range(len(myList)):
        for j in range(0, len(myList)-i-1):
            if myList[j] > myList[j+1]:
                # swap greater element with smaller one
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
                # another way of swapping elements
                # myList[j], myList[j+1] = myList[j+1], myList[j]

myList5 = [2,10,8,5,15,30,17,9,41,13,20,54]
bubbleSort(myList5)
print("5- bubble sort of my list is: ",myList5)