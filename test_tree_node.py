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

    def test_get_value(self):
        """
         - test get_value implementation
         - checks if value return is same as implementation
        """
        value = 5
        node = TreeNode(value=value)
        self.assertEqual(node.get_value(), value)

    def test_get_left(self):
        """
         - test get_left implementation
         - returns True if variable exists after instantiation
        """
        value = 5
        left = TreeNode()
        right = TreeNode()
        node = TreeNode(value=value, left=left, right=right)
        self.assertEqual(node.get_left(), left)
   
    def test_get_right(self):
        """
         - test get_right implementation
         - returns True if variable exists after instantiation
        """
        value = 5
        left = TreeNode()
        right = TreeNode()
        node = TreeNode(value=value, left=left, right=right)
        self.assertEqual(node.get_right(), right)

    def test_get_parent(self):
        """
         - test get_right implementation
         - returns True if variable exists after instantiation
        """
        parent = TreeNode()
        node = TreeNode(parent=parent)
        self.assertEqual(node.get_parent(), parent)

if __name__ == '__main__':
    unittest.main()
