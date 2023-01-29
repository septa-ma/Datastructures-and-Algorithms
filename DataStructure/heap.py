# what is heap?
# a tree data structure that can be represented in a form of an array. 
# it is used to implement priority queues.
# what is complete binary tree?
# a special type of binary tree where all the levels of the tree are 
# filled completely except the lowest level nodes which are filled 
# from as left as possible.
# heap is a complete binary tree means that in each level should not 
# have any missing (specially in left-child) if represented as an array 
# should not have any gaps. in this representation for arr[i]:
# - root element -> arr[0] 
# - its parent node -> arr[(i -1) / 2]
# - its left child node -> arr[(2 * i)]
# - its right child node -> arr[(2 * i) + 1]
# another definition, a tree which is a full complete binary tree 
# in (hight-1) level.
# types of heap:
# 1- max heap -> every root's value is greatest than all child nodes.
# 2- min heap -> every root's value is smallest than all child nodes.
# one of the most important opration of heap is heapify which should apply 
# after any insertion and deletion node.
# it is the process to rearrange the elements to maintain the property of 
# heap data structure.

class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
        # self.root = 1
    
    # find the index of parent for the current node
    def parent(self, index):
        return index//2

    # find the index of left-child for the current node
    def leftChild(self, index):
        return (2 * index) 

    # find the index of right-child for the current node
    def rightChild(self, index):
        return (2 * index) + 1

    # check if the node is a leaf
    def isLeaf(self, index):
        return index*2 > self.size

    # swap two nodes
    def swap(self, firstIndex, secondIndex):
        self.heap[firstIndex], self.heap[secondIndex] = self.heap[secondIndex], self.heap[firstIndex]

    # print the heap
    def showHeap(self):
        for i in range(1, (self.size//2)+1):
            print(
                "PARENT : " + str(self.heap[i]) + 
                " LEFT CHILD : " + str(self.heap[self.leftChild(i)]) + 
                " RIGHT CHILD : " + str(self.heap[self.rightChild(i)])
                )

class MinHeap():
    # create an object of super class
    minHeap = Heap()

    # min heap insertion
    def minInsertion(self, data):
        self.minHeap.heap.append(data)
        self.minHeap.size += 1
        # if the data is less than its parent swap the datas
        current = self.minHeap.size
        while self.minHeap.heap[current] < self.minHeap.heap[self.minHeap.parent(current)]:
            self.minHeap.swap(current, self.minHeap.parent(current))
            current = self.minHeap.parent(current)
        # print(self.minHeap.heap)

     # min heapify
    def minHeapify(self, index):
        minChild = 0
        # if the node is a non-leaf node
        while not self.minHeap.isLeaf(index) and self.minHeap.size > 0:
            leftChild = self.minHeap.leftChild(index)
            rightChild = self.minHeap.rightChild(index)
            # find the min child
            if self.minHeap.heap[leftChild] < self.minHeap.heap[rightChild]:
                minChild = leftChild
            else:
                minChild = rightChild
            # swap node with its min child
            if self.minHeap.heap[index] > self.minHeap.heap[minChild]:
                self.minHeap.swap(index, minChild)
            index = minChild

    # min heap deletion
    def minDeletion(self):
        if len(self.minHeap.heap) == 1:
            return "empty heap"
        # save root (value at index 1 is root)
        root = self.minHeap.heap[1]
        # move the last value of the heap to the root
        self.minHeap.heap[1] = self.minHeap.heap[self.minHeap.size]
        # decrease the size of the heap
        self.minHeap.size -= 1
        # move down the root to keep the heap property
        self.minHeapify(1)
        return root

    # show min heap
    def showHeap(self):
        return self.minHeap.showHeap()

class MaxHeap():
    # create an object of super class
    maxHeap = Heap()
    # in max heap it should be a big number
    maxHeap.heap[0] = 9999999

    # max heap insertion
    def maxInsertion(self, data):
        self.maxHeap.heap.append(data)
        self.maxHeap.size += 1
        # if the data is less than its parent swap the datas
        current = self.maxHeap.size
        while self.maxHeap.heap[current] > self.maxHeap.heap[self.maxHeap.parent(current)]:
            self.maxHeap.swap(current, self.maxHeap.parent(current))
            current = self.maxHeap.parent(current)

    # max heapify
    def maxHeapify(self, index):
        maxChild = 0
        # if the node is a non-leaf node
        while not self.maxHeap.isLeaf(index) and self.maxHeap.size > 0:
            leftChild = self.maxHeap.leftChild(index)
            rightChild = self.maxHeap.rightChild(index)
            # find the max child
            if self.maxHeap.heap[leftChild] > self.maxHeap.heap[rightChild]:
                maxChild = leftChild
            else:
                maxChild = rightChild
            # swap node with its max child
            if self.maxHeap.heap[index] < self.maxHeap.heap[maxChild]:
                self.maxHeap.swap(index, maxChild)
            index = maxChild
    
    # max heap deletion
    def maxDeletion(self):
        if len(self.maxHeap.heap) == 1:
            return "empty heap"
        # save root (value at index 1 is root)
        root = self.maxHeap.heap[1]
        # move the last value of the heap to the root
        self.maxHeap.heap[1] = self.maxHeap.heap[self.maxHeap.size]
        # decrease the size of the heap
        self.maxHeap.size -= 1
        # move down the root to keep the heap property
        self.maxHeapify(1)
        return root

    # show max heap
    def showHeap(self):
        return self.maxHeap.showHeap()


minheap = MinHeap()
minheap.minInsertion(5)
minheap.minInsertion(3)
minheap.minInsertion(17)
minheap.minInsertion(10)
minheap.minInsertion(84)
minheap.minInsertion(1)
minheap.minInsertion(19)
minheap.minInsertion(6)
minheap.minInsertion(22)
minheap.minInsertion(9)
minheap.minInsertion(8)
minheap.showHeap()
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
print("Min value is " + str(minheap.minDeletion()))
minheap.showHeap()
print("**** End Min Heap *****\n")
maxheap = MaxHeap()
maxheap.maxInsertion(5)
maxheap.maxInsertion(3)
maxheap.maxInsertion(17)
maxheap.maxInsertion(10)
maxheap.maxInsertion(84)
maxheap.maxInsertion(1)
maxheap.maxInsertion(19)
maxheap.maxInsertion(6)
maxheap.maxInsertion(22)
maxheap.maxInsertion(9)
maxheap.maxInsertion(8)
maxheap.showHeap()
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
print("Max value is " + str(maxheap.maxDeletion()))
maxheap.showHeap()
print("**** End Max Heap *****")
