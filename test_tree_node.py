import unittest
from tree_node import TreeNode


class TreeNodeTest(unittest.TestCase):

    def test_object(self):
        """
          - test if node object has been implemented
          - returns true for the correct name
        """
        node = TreeNode()
        self.assertEqual(type(node).__name__, 'TreeNode')
     
    def test_init_node(self):
        """
         - test init implementation
         - returns True if variable exists after instantiation
        """
        value = 5
        left = TreeNode()
        right = TreeNode()
        parent = TreeNode()
        node = TreeNode(value=value, left=left, right=right, parent=parent)
        
        self.assertEqual(type(node), type(TreeNode()))
        self.assertEqual(type(node.left), type(TreeNode()))
        self.assertEqual(type(node.right), type(TreeNode()))
        self.assertEqual(type(node.parent), type(TreeNode()))


if __name__ == '__main__':
    unittest.main()
