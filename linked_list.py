"""
 - Python implementation of doubly linked-list with sentinel
 - insert is always at the begining just behind the sentinel 
 Methods implemented:
  - search(k)
  - insert(x)
  - delete(x)
"""
from node import Node


class LinkedList(object):
    
    def __init__(self):
        self.head = Node()
    
    def insert(self, key):
        node = Node(key=key)
        if self.head.next is None:
            self.head.next = node
            node.prev = self.head
        else:
            temp = self.head.next
            self.head.next = node
            node.next = temp
            node.prev = self.head
            temp.prev = node
    
    def search(self, key):
        found = False
        current = self.head.next
        try: 
            while not found:
                if current.get_key() == key:
                    found = True
                else:
                    current = current.next
            return current
        except AttributeError:
            raise KeyNotFoundError("key not in linked list")

    def delete(self, node):
        prev = node.prev
        if node.next:
           """
              - case when node has a link following it
           """
           prev.next = node.next
           node.next.head = prev
        else:
          """
              - case when node does not have a link following it
          """
          prev.next = None


class KeyNotFoundError(Exception):
    """ Raised when key in search is not found """
    pass
