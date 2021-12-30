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

    def test_append(self):
        # 연결리스트에 데이터 링크를 추가 테스트
        self.linkedList.append("TEST")
        self.assertEqual(self.linkedList[0], "TEST")

    def test_insert(self):
        # 특정 인덱스번호 뒤에 데이터를 삽입하는 테스트
        test_list = list(range(5))

        # 더미데이터를 연결리스트에 삽입
        for data in test_list:
            self.linkedList.append(data)

        # 연결리스트 중간에 값 삽입
        self.linkedList.insert(2, "TEST")

        self.assertEqual(self.linkedList[2], "TEST")



if __name__ == '__main__':
    unittest.main()
