import unittest
from my_collections.binaryTree import BinaryTree, Node
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
        root = Node(10)
        root.left = Node(8)
        root.right = Node(9)
        root.left.left = Node(6)
        root.left.right = Node(7)
        root.right.left = Node(5)

        self.binaryTree.root = root
        self.binaryTree.call_pre_order()


if __name__ == '__main__':
    unittest.main()
