# what is searching?
# check or retrieve an element from any data structure.
# classified into two categories:
# 1- sequential search -> a sequential search is made over all items 
# one by one. every item is checked and if a match is found then that particular 
# item is returned, otherwise the search continues till the end of the data structure.
# 2- interpolation search -> repeatedly target the center of the search structure and 
# divide the search space in half. works on the probing position of the required
# value. the data collection should be in a sorted form and equally distributed.
# this process continues on the sub-array as well until the size of subarray
# reduces to zero.

# 1- sequential search - linear search
def linearSearch(myList, data):
    pos = 0
    for i in range(len(myList)):
        if myList[i] == data:
            pos = i
    return "Found "+str(data)+" at index "+str(pos)

myList1 = [11, 25, 5.5, 78, 13]
print(linearSearch(myList1, 5.5))

# 2-1 interpolation search - binary search - recursive function
def interpolationSearch(myList, low, high, data):
    # check if the array is sorted
    while low <= high and myList[low] <= data and myList[high] >= data:
        # calculating the position
        pos = (high + low) // 2
        # check if the pos value is equal with data
        if myList[pos] == data:
            return "Found "+str(data)+" at index "+str(pos)
        # check the data in right sub-list
        if myList[pos] < data:
            return interpolationSearch(myList, pos+1, high, data)
        # check the data in left sub-list
        if myList[pos] > data:
            return interpolationSearch(myList, low, pos-1, data)
    # data not found
    return str(data)+" is not found"

myList2 = [2, 6, 11, 19, 27, 31, 45, 121]
low = 0
high = len(myList2) - 1
data = 45
print(interpolationSearch(myList2, low, high, data))

# 2-2 interpolation search - binary search - iterative function
def binarySearch(myList, low, high, data):
    # check if the array is sorted
    while low <= high and myList[low] <= data and myList[high] >= data:
        # calculating the position 
        pos = low + (high - low) // 2 # way 1
        # pos = high - (high - low) // 2 # way 2
        # check if the pos value is equal with data
        if myList[pos] == data:
            return "Found "+str(data)+" at index "+str(pos)
        # ignore right sub-list
        if myList[pos] < data:
            low = pos+1
        # ignore the left sub-list
        else:
            high = pos-1
    # data not found
    return str(data)+" is not found"

myList3 = [2, 6, 10, 11, 19, 27, 31, 45, 121]
low = 0
high = len(myList3) - 1
data = 19
print(binarySearch(myList3, low, high, data))

# 2-3 interpolation search - ternary search 
# it is similar to binary search. The only difference is that, we divide the 
# given array into three parts and determine which has the key. it reduces the 
# time complexity a bit more. 
def ternarySearch(myList, low, high, data):
    # check if the array is sorted
    while low <= high and myList[low] <= data and myList[high] >= data:
        # find 2 positions
        pos1 = low + (high - low) // 3
        pos2 = high - (high - low) // 3
        # check if data is at positions
        if myList[pos1] == data:
            return "Found "+str(data)+" at index "+str(pos1)
        if myList[pos2] == data:
            return "Found "+str(data)+" at index "+str(pos2)
        # if data is not at positions, check in which sub-list it is present
        # then repeat the search operation in that sub-list
        if myList[pos1] > data:
            return ternarySearch(myList, low, pos1-1, data)
        elif myList[pos2] < data:
            return ternarySearch(myList, pos2+1, high, data)
        else:
            return ternarySearch(myList, pos1+1, pos2-1, data)
    # data not found
    return str(data)+" is not found" 

myList4 = [2, 6, 10, 11, 19, 27, 31, 45, 50, 62, 121]
low = 0
high = len(myList4) - 1
data = 50
print(binarySearch(myList4, low, high, data))