"""
 - Python implementation of node for trees
 - methods implemented
   - get_value
   - get_left
   - get_right
   - get_parent
"""

class TreeNode(object):
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent
