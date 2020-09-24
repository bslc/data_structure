import pdb
import unittest
from linked_list import LinkedList
from linked_list import KeyNotFoundError


class LinkedListTest(unittest.TestCase):

    def test_object(self):
        """
          - test if linked_list object has been implemented
          - returns true for the correct name
          - returns empty linked list with None in head
        """
        linked_list = LinkedList()
        self.assertEqual(type(linked_list).__name__, 'LinkedList')
        self.assertEqual(type(linked_list.head).__name__, 'Node')
        self.assertEqual(linked_list.head.key, None)

    def test_insert(self):
        """
          - test if insert has been implemented correctly
          - return head with type Node 
        """
        linked_list = LinkedList()
        key = 5
        linked_list.insert(key)
        self.assertEqual(linked_list.head.next.key, 5)

    def test_insert_with_multiple_linked(self):
        """
          - test when there are multiple links on the list
          - return the correct key
        """
        linked_list = LinkedList()
        key_1 = 5
        key_2 = "foo"
        linked_list.insert(key_1)
        linked_list.insert(key_2)
        self.assertEqual(linked_list.head.next.key, key_2)
        self.assertEqual(linked_list.head.next.next.key, key_1)

    def test_node_insert_link_to_prev(self):
        """ 
         - test if node points to prev 
         - return the correct node
        """
        linked_list = LinkedList()
        key_1 = 5
        key_2 = "foo"
        linked_list.insert(key_1)
        linked_list.insert(key_2)
        node_1 = linked_list.search(key_1)
        node_2 = linked_list.search(key_2)
        self.assertEqual(node_1.prev.key, key_2)
        self.assertEqual(node_2.prev.key, None)

    def test_search(self):
        """
          - test when there are multiple links on the list
          - return the correct key
        """
        linked_list = LinkedList()
        key_1 = 5
        key_2 = "foo"
        linked_list.insert(key_1)
        linked_list.insert(key_2)
        node = linked_list.search(key_1)
        self.assertEqual(node.key, key_1)
        node = linked_list.search(key_2)
        self.assertEqual(node.key, key_2)
        self.assertRaises(KeyNotFoundError, linked_list.search, 'bar')

    def test_delete(self):
        """
          - test if delete node has been impleted correctly
          - return true if the node cannot be found via search
        """
        linked_list = LinkedList()
        key_1 = 5
        key_2 = "foo"
        key_3 = "meow"
        linked_list.insert(key_1)
        linked_list.insert(key_2)
        linked_list.insert(key_3)
        node = linked_list.search(key_1)
        linked_list.delete(node)
        self.assertRaises(KeyNotFoundError, linked_list.search, 5)
        node = linked_list.search(key_2)
        self.assertEqual(node.next, None)
        node_3 = linked_list.search(key_3)
        linked_list.delete(node_3)
        self.assertEqual(linked_list.head.next, node)
 

if __name__ == '__main__':
    unittest.main()
