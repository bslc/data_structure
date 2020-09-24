import unittest
from node import Node


class NodeTest(unittest.TestCase):

    def test_object(self):
        """
          - test if node object has been implemented
          - returns true for the correct name
        """
        node = Node()
        self.assertEqual(type(node).__name__, 'Node')
     
    def test_init_node(self):
        """
         - test init implementation
         - returns True if variable exists after instantiation
        """
        node_prev = Node(key=1)
        node_next = Node(key=2)
        key = 5
        node = Node(node_prev, key, node_next)
        
        self.assertEqual(node.key, key)
        self.assertEqual(node.prev, node_prev)
        self.assertEqual(node.next, node_next)


if __name__ == '__main__':
    unittest.main()
