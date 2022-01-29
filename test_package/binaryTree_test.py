import unittest
from my_collections.binaryTree import BinaryTree
from random import randint


class MyTestCase(unittest.TestCase):
    # TEST CASE
    __tc = 0

    # 1부터 10까지 중 랜덤한 테스트 케이스가 주어진다.
    # 트리를 초기화 한다.
    def setUp(self):
        self.__tc = randint(1, 10)
        self.binaryTree = BinaryTree()

    def test_init(self):
        self.assertEqual(type(self.binaryTree), BinaryTree)  # add assertion here

    def test_insert(self):
        pass


if __name__ == '__main__':
    unittest.main()
