# what is an array?
# an array is a data structure that holds fix number of elements
# and these elements should be of the same data type.
# there are tow types of array: 
# static array -> has fix size and dynamic array -> has flexible size (in python we call it list)
# basic terminologies of array are:
# array-index -> in an array, elements are identified by their indexes. it starts from 0.
# array-element -> elements are items stored in an array and can be accessed by their index.
# array-length -> the length of an array is determined by the number of elements it can contain.
# declaration means allocating memory for an array of a given size.

# 1- Declare an array
import array
myArr = array.array('i', [2,5,7,4,6,1,3,9])

# 2- insert item into array
myArr.insert(1, 205) # add the value(x) at the ith position -> insert(i, x)
myArr.append(80) # add the value at the end of array
print ("New created array after insert is : ")
for i in range (0,len(myArr)):
    print(myArr[i], end=" ")

# 3- Remove item
print (myArr.pop(5)) # omit value of ith position
myArr.remove(4) # omit x value
print ("New created array after removeing is : ")
for i in range (0,len(myArr)):
    print(myArr[i], end=" ")

# 4- Reverse an array
def reverse(myArray):
    l = len(myArray)
    i = -1
    while(i >= -l):
        yield myArray[i]
        i -= 1

result = array.array('i', [])
for item in reverse(myArr):
    result.append(item)

print("\nNew created array after reverseing is: ")
for i in range (0,len(result)):
    print(result[i], end=" ")

myArr.reverse() # reverse the array
print ("\nNew created array after reverseing is : ")
for i in range(0, len(myArr)):
    print(myArr[i], end=" ")

# 5- Find index
print('\n',myArr.index(80)) # find the ith position of value(x)
