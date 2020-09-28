"""
Python implementation of a stack based on CLSR pg 232-233

the following function
 - is_empty
 - pop
 - push
"""


class StackUnderflowError(Exception):
    
    def __init__(self, *args, **kwargs):
        msg = "Stack is empty."
        Exception.__init__(self, msg, **kwargs) 


class Stack(object):

    def __init__(self):
        self.data = []

    def is_empty(self):
        """ check if stack is empty """
        if self.data:
            return False
        return True 

    def push(self, entry):
        """ insert element into stack """
        self.data.append(entry)

    def pop(self):
        """ 
          check if stack is empty
          remove top element if it is not
        """
        if self.is_empty():
            raise StackUnderflowError
        else:
          temp = self.data[-1] 
          self.data.remove(temp)
          return temp
