import unittest
from queue import Queue 

class QueueTest(unittest.TestCase):
    def test_object(self):
        """
          - test if queue object has been implemented
          - returns true for the correct name
        """
        queue = Queue()
        self.assertEqual(type(queue).__name__, 'Queue')

    def test_has_list(self):
        """
          - test if queue has internal list to store data
          - returns true if it variable is a list
        """
        queue = Queue()
        self.assertTrue(type(queue.data) is list)


    def test_enqueue(self):
        """
          - test if enqueue has been implemented correctly
          - returns true on checking element in self list
        """
        queue = Queue()
        data1 = 'foo'
        queue.enqueue(data1)
        data2 = 'bar'
        queue.enqueue(data2)
        self.assertEqual(queue.data[0], data1) 
        self.assertEqual(queue.data[-1], data2) 

    def test_dequeue(self):
        """
        self.assertEqual(queue.data[0], data1) 
          - test if pop has been implemented correctly
          - returns true when data is not in list
        """
        queue = Queue()
        data1 = 'foo'
        data2 = 'bar'
        queue.enqueue(data1)
        queue.enqueue(data2)
        check1 = queue.dequeue()
        check2 = queue.dequeue()
        self.assertEqual(data1, check1)
        self.assertEqual(data2, check2)


if __name__ == '__main__':
    unittest.main()
