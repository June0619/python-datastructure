import unittest
from my_collections.stack import Stack
import inspect
from random import *


class MyTestCase(unittest.TestCase):

    __tc = 0

    # Given
    # 1. 1부터 10사이의 랜덤한 정수형 Test case 하나가 주어진다.
    # 2. 스택을 1에서 정한 tc 사이즈로 초기화 한다.
    def setUp(self):
        self.__tc = randint(1, 10)
        self.stack = Stack(self.__tc)

    # 스택 최대 사이즈가 setUp 함수 동작시에 생성한 랜덤한 정수와 같은지 테스트
    def test_stack_size(self):
        self.assertEqual(self.stack.max_stack_size, self.__tc)

    # push 와 pop 함수 정상 동작여부 (push 한 자료와 pop 한 자료가 동일한지)
    def test_push_pop(self):
        self.stack.push("A")
        self.assertEqual(self.stack.pop(), "A")

    # is_full 함수 동작여부
    def test_full(self):
        for idx in range(self.__tc):
            self.stack.push(idx)
        self.assertEqual(self.stack.is_full(), True)

    # is_empty 함수 동작여부
    def test_empty(self):
        self.stack.push(1).push(2)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.is_empty(), True)

    def tearDown(self):
        del self.stack


if __name__ == '__main__':
    unittest.main()
