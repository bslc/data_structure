"""
  Python implementaiton of a doubly linked list node
    - node object has prev, key, and next
"""


class Node(object):
    def __init__(self, prev=None, key=None, next=None):
        self.prev = prev
        self.key = key
        self.next = next
