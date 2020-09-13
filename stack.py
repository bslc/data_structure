"""
Python implementation of a stack.

the following function
 - is_empty
 - pop
 - push
"""

class Stack(object):

    def __init__(self):
        self.data = []

    def is_empty(self):
        if self.data:
            return False
        return True 

    def push(self, entry):
        self.data.append(entry)

    def pop(self):
        temp = self.data[-1] 
        self.data.remove(temp)
        return temp
