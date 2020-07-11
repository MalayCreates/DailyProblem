###########################################
# Author: Malay Agarwal
# Problem: 
# . Implement a data structure to 
# accomplish this, with the following API:
# record(order_id): adds the order_id to 
# the log
# get_last(i): gets the ith last element 
# from the log. i is guaranteed to be 
# smaller than or equal to N.
###########################################

class CircQueue:
    def __init__(self, size):
        self.size = size
        self.data = [None for i in range(size)]
        self.front, self.rear = None, None


    def record(self, order_id):
        if(self.front is None):
            self.front, self.rear = 0, -1
        elif((self.rear+1)%self.size == self.front):
            self.front = (self.front+1)%self.size
        self.rear = (self.rear+1)%self.size
        self.data[self.rear] = order_id


    def get_last(self, i):
        index = (self.front + self.size - i)%self.size
        return self.data[index]

queue = CircQueue(3)
queue.record(1)
queue.record(2)
queue.record(3)
queue.record(4)
queue.record(5)
queue.record(6)
print (queue.get_last(2))
print (queue.get_last(1))