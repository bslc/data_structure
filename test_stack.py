import unittest
from stack import Stack
from stack import StackUnderflowError 

class StackTest(unittest.TestCase):

    def test_object(self):
        """
          - test if stack object has been implemented
          - returns true for the correct name
        """
        stack = Stack()
        self.assertEqual(type(stack).__name__, 'Stack')

    def test_has_list(self):
        """
          - test if stack has internal list to store data
          - returns true if it variable is a list
        """
        stack = Stack()
        self.assertTrue(type(stack.data) is list)

    def test_is_emtpy(self):
        """
          - test if is_empty has been implemented correctly
          - returns true on checking on an new stack
          - returns false on check when there is data
        """
        stack = Stack()
        self.assertTrue(stack.is_empty())
        data = 'foo'
        stack.push(data)
        self.assertFalse(stack.is_empty())

    def test_push(self):
        """
          - test if push has been implemented correctly
          - returns true on checking element in self list
        """
        stack = Stack()
        data = 'foo'
        stack.push(data)
        self.assertTrue(data in stack.data)

    def test_pop(self):
        """
          - test if pop has been implemented correctly
          - returns true when data is not in list
        """
        stack = Stack()
        data1 = 'foo'
        data2 = 'bar'
        stack.push(data1)
        stack.push(data2)
        check2 = stack.pop()
        check1 = stack.pop()
        self.assertEqual(data1, check1)
        self.assertEqual(data2, check2)
        self.assertTrue(stack.is_empty())

    def test_pop_empty(self):
        """
          - test pop if stack is empty
          - returns underflow error
        """
        stack = Stack()
        self.assertRaises(StackUnderflowError, stack.pop)

if __name__ == '__main__':
    unittest.main()
