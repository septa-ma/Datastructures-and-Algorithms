# what is queue?
# think about a line of people in a backery or any service 
# that you're waiting for, is queue.
# for adding a item enqueue() it to the end of the queue.
# for removing a item dequeue() it from head of the queue.
# removing called FIFO first in first out.

# make a queue with list structure
class Queue:
    def __init__(self):
        self.myQueue = []
    
    # get size of the queue
    def length(self):
        size = len(self.myQueue)
        return size

    def enqueue(self, data):
        # insert an uniqe data at the end of the list
        if(data not in self.myQueue):
            self.myQueue.append(data)
            return self.myQueue
        return False

    def dequeue(self):
        if(self.length != 0):
            # remove a data from head of the list 
            result = self.myQueue.pop(0)
            return result, self.myQueue
        return False

# q = Queue()
# print(q.enqueue(10))
# print(q.enqueue(20))
# print(q.enqueue(30))
# print(q.enqueue(40))
# print(q.enqueue(50))
# print(q.enqueue(60))
# print()
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.enqueue(80))
