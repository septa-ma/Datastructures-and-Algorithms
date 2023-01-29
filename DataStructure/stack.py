# what is stack?
# it likes a plate of pancakes, which eat from the last one.
# not only adding an element at the end of the stack but also removing
# an element there, removing is called LIFO last in first out.
# for adding an element use push() and for removing use pop().

# make a stack with list
class Stack:
    def __init__(self):
        self.myStack = []

    # get size of the queue
    def length(self):
        size = len(self.myQueue)
        return size

    def push(self, data):
        # insert an uniqe data at the end of the list
        if(data not in self.myStack):
            self.myStack.append(data)
            return self.myStack
        return False

    def pop(self):
        if(self.length != 0):
            # remove a data from head of the list 
            result = self.myStack.pop()
            return result, self.myStack
        return False

    def peek(self):
        if(self.length != 0):
            # peek the top item of stack
            return self.myStack[-1]
        return False


# s = Stack()
# print(s.push(10))
# print(s.push(20))
# print(s.push(30))
# print(s.push(40))
# print(s.push(50))
# print()
# print(s.peek())