import unittest
from my_collections.stack import Stack
import inspect
from random import *


class MyTestCase(unittest.TestCase):

    __tc = 0

    def setUp(self):
        self.__tc = randint(1, 10)
        self.stack = Stack(self.__tc)

    def test_stack_size(self):
        self.assertEqual(self.stack.max_stack_size, self.__tc)
        print(f'{inspect.stack()[0][3]}() is pass')

    def test_push(self):
        self.stack.push("A")
        self.assertEqual(self.stack.pop(), "A")

    def tearDown(self):
        del self.stack


if __name__ == '__main__':
    unittest.main()
