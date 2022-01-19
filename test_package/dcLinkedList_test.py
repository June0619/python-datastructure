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
        # 데이터 여러개 추가 시 tail 과 head 연결 테스트
        self.dcLinkedList.append("TEST1")
        self.dcLinkedList.append("TEST2")
        self.assertEqual(self.dcLinkedList[0].next, self.dcLinkedList[1])
        self.assertEqual(self.dcLinkedList[1].prev, self.dcLinkedList[0])

    def test_insert(self):
        self.dcLinkedList.append(1).append(2).insert(1, 99)
        self.dcLinkedList.to_string()

        self.assertEqual(99, self.dcLinkedList[1].data)
        self.assertEqual(3, self.dcLinkedList.length)

        # Index Err Test
        self.assertRaises(IndexError, self.dcLinkedList.insert, 4, 'err')

    def test_get_item(self):
        self.dcLinkedList.append(1)
        self.dcLinkedList.append(2)
        self.dcLinkedList.append(3)
        self.assertEqual(3, self.dcLinkedList[2].data)

    def test_remove(self):
        self.dcLinkedList.append(1).append(2).append(3)

        self.assertEqual(2, self.dcLinkedList.remove(1))

        self.assertEqual(3, self.dcLinkedList[1].data)
        self.assertEqual(2, self.dcLinkedList.length)

    def tearDown(self):
        del self.dcLinkedList


if __name__ == '__main__':
    unittest.main()
