import unittest
from my_collections.doubly_circular_linked_list import DoublyCircularLinkedList
from random import *


class MyTestCase(unittest.TestCase):

    __tc = 0

    # 1. 1부터 10사이의 랜덤한 정수형 Test case 하나가 주어진다.
    # 2. 빈 연결리스트를 생성한다.
    def setUp(self):
        self.__tc = randint(1, 10)
        self.dcLinkedList = DoublyCircularLinkedList()

    def test_append(self):
        # 연결리스트에 데이터 링크를 추가 테스트
        self.dcLinkedList.append("TEST")
        self.assertEqual(self.dcLinkedList[0].data, "TEST")
        self.assertEqual(self.dcLinkedList[0].next, self.dcLinkedList[0])
        self.assertEqual(self.dcLinkedList[0].prev, self.dcLinkedList[0])

    def test_append_twice(self):
        # 연결리스트에 데이터 링크를 추가 테스트
        self.dcLinkedList.append("TEST1")
        self.dcLinkedList.append("TEST2")
        self.assertEqual(self.dcLinkedList[0].next, self.dcLinkedList[1])
        self.assertEqual(self.dcLinkedList[1].prev, self.dcLinkedList[0])

    def tearDown(self):
        del self.dcLinkedList


if __name__ == '__main__':
    unittest.main()
