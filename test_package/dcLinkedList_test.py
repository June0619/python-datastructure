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

    def test_insert(self):
        # 특정 인덱스번호 뒤에 데이터를 삽입하는 테스트
        test_list = list(range(5))

        # 더미데이터를 연결리스트에 삽입
        for data in test_list:
            self.linkedList.append(data)

        # 연결리스트 중간에 값 삽입
        self.linkedList.insert(2, "TEST")
        self.assertEqual(self.linkedList[2], "TEST")

    def test_delete(self):
        # 연결리스트 내 특정 인덱스 값을 삭제하는 테스트
        test_list = list(range(5))

        # 더미데이터를 연결리스트에 삽입
        for data in test_list:
            self.linkedList.append(data)

        # 연결리스트 특정 인덱스 값 삭제
        self.linkedList.delete(2)
        # 연결리스트의 데이터 갯수가 4개가 되는지 테스트
        self.assertEqual(self.linkedList.length, 4)
        # 연결리스트 2번 인덱스의 데이터가 3인지 테스트
        self.assertEqual(self.linkedList[2], 3)

        self.linkedList.to_string()

        # 연결리스트 마지막 인덱스 값 삭제
        self.linkedList.delete(3)
        # 연결리스트의 데이터 갯수가 3개가 되는지 테스트
        self.assertEqual(self.linkedList.length, 3)

        self.linkedList.to_string()

    def tearDown(self):
        del self.dcLinkedList


if __name__ == '__main__':
    unittest.main()
