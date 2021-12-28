import unittest
from my_collections.linked_list import LinkedList
from random import *


class MyTestCase(unittest.TestCase):

    __tc = 0

    # Given
    # 1. 1부터 10사이의 랜덤한 정수형 Test case 하나가 주어진다.
    # 2. 빈 연결리스트를 생성한다.
    def setUp(self):
        self.__tc = randint(1, 10)
        self.linkedList = LinkedList()

    def test_add(self):
        # 연결리스트에 데이터 링크를 추가 테스트
        self.linkedList.add("TEST")
        self.assertEqual(self.linkedList[0], "TEST")


if __name__ == '__main__':
    unittest.main()
