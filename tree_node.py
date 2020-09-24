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
