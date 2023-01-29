# what is hash table?
# it's a key-value data structure (maps keys to values).
# you can find your key or value immediately that the search and insertion function. 
# of a data is constant time -> O(1) and linner time for a terriable time -> O(n).
# you can use any types of data structure for keys or values.
# it could be a good solution for any problems.
# components of hashing:
# key -> it's an index or location for storage of an item, it can be anything -
# - string or integer which is fed as input in the hash function.
# hash function -> a function that converts a given numeric or alphanumeric key-
# -and do some calculation to find the exact position of the key in the memory-
# -then returns the index of an element.
# collision -> whenever two keys have the same hash value.
# seprate chaining -> a way for handling collision make a Linked List at each- 
# -index which containing all keys for a given index.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class HashTable:
    # initialize a hashtable
    def __init__(self, initCapacity):
        self.capacity = initCapacity
        self.size = 0
        self.bucket = [None]*self.capacity

    def hashFunction(self, key):
        hashsum = 0 
        # use enumerate() to get a iterable value
        # use ord for changeing string to a numeric value
        for i, curChar in enumerate(key):
            hashsum += (i + len(key)) ** ord(curChar)
            hashsum = hashsum % self.capacity
        yield hashsum

    def insertation(self, key, value):
        # increase the size of hashtable
        self.size += 1
        # make a new node for inserting
        newNode = Node(key, value) 
        # calculate hash of the key
        for item in self.hashFunction(key):
            index = item
        # get the current node of the hash
        # if it's None assign new node to it
        node = self.bucket[index]
        if node is None:
            self.bucket[index] = newNode
            return True
        # if it's not None loop through linkedlist and add 
        # the new node to end of the linkedlist at the index
        preNode = None
        while node is not None:
            preNode = node # save the current node to not be losed
            node = node.next # go for next node to be checked
        preNode.next = newNode
        return True

    def deletation(self, key):
        # calculate hash of the key
        for item in self.hashFunction(key):
            index = item
        # get the current node of the hash
        node = self.bucket[index]
        preNode = None
        # loop through linkedlist and delete pointer of previous 
        # node and selection node by makeing a pointer between 
        # previous node and next node of selection
        while node:
            if node.key == key:
                self.size -= 1
                if preNode is None:
                    self.bucket[index] = node.next
                preNode.next = preNode.next.next
                return True
            preNode = node # save the current node to not be losed
            node = node.next # go for next node to be checked

    def searching(self, key):
        for item in self.hashFunction(key):
            index = item
        # get the current node of the hash
        node = self.bucket[index]
        # loop through linkedlist till the last node
        while node:
            if node.key == key:
                return node.key, node.value
            node = node.next # go for next node to be checked


# # make a hash table
# ht = HashTable(20)
# # insert data
# ht.insertation('a','aa')
# ht.insertation('12a','aa')
# ht.insertation('ok','aa')
# ht.insertation('1b','bb')
# # search and delete a key
# print(ht.searching('1b'))
# print(ht.deletation('1b'))
# print(ht.searching('1b'))
