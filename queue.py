"""
Python implementation of a queue. 

Queue is first-in first-out. 

Methods implemented:

 - enqueue
 - dequeue

"""
class Queue(object):
    def __init__(self):
        self.data = []

    def enqueue(self, entry):
        self.data.append(entry)

    def dequeue(self):
        temp = self.data[0]
        self.data.remove(temp)
        return temp
