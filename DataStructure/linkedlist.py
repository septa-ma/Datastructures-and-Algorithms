# what is linkedlist?
# a linkedlist is a data structure which looks like a chain of nodes, 
# where each node is a different element.
# each node contains 2 patrs a data and a pointer to the next node in the chain.
# the position of each node doesn't matter in the memory.
# there is a head pointer, which points to the first element of the linked list, 
# and if the list is empty then it simply points to null or nothing.
# searching is slow and it costs O(n).

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, node):
        self.head = node

# get the length of a linkedlist
    def linkedlistlen(self):
        length = 0
        node = self.head
        while node != None:
            length += 1
            node = node.next
        return length

    def insertation(self, data, index):
        newNode = Node(data)
        curNode = self.head # start from head of linkedlist
        preNode = None # initialize preNode for following the way
        # loop through linkedlist to find current node and add new one
        for i in range(0, self.linkedlistlen()):
            preNode = curNode # save the current node to not be losed
            curNode = curNode.next # go for next node to be checked
            if(i == index):
                preNode.next = newNode
                newNode.next = curNode
                return True

    def deletation(self, data):
        curNode = self.head # start from head of linkedlist
        preNode = None # initialize preNode for following the way
        # loop through linkedlist till the last node
        # if find the selection node
        # delete pointer of previous node and selection node
        # by makeing a pointer between previous node and next node of selection
        while curNode:
            if(curNode.data == data):
                preNode.next = curNode.next
                curNode = None
                return True
            preNode = curNode # save the current node to not be losed
            curNode = curNode.next # go for next node to be checked

    def searching(self, data):
        curNode = self.head # start from head of linkedlist
        index = 0
        # loop through linkedlist till the last node
        while curNode:
            if(curNode.data == data):
                return True, index
            curNode = curNode.next # go for next node to be checked
            index += 1


# # make a linkedlist
# myList = LinkedList(Node(10, Node(20, Node(30, Node(40)))))
# # insert new node
# print(myList.insertation(110, 1))
# print(myList.linkedlistlen())
# # delete a node
# print(myList.deletation(30))
# print(myList.linkedlistlen())
# # find a node
# print(myList.searching(40)) 