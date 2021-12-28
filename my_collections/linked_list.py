class Node:
    """
    연결리스트 내부에서 노드를 담당할 클래스
    1. 멤버 변수
        1-1. 데이터
        1-2. 다음 노드 주소를 저장할 변수
    2. 멤버 함수
        2-1. 초기화(데이터)
            인자로 받는 데이터를 가진 노드를 생성한다. (링크부는 Null 값)
    """
    __data = None
    __next = None

    def __init__(self, p_data):
        self.__data = p_data


class LinkedList:
    """
    1. LinkedList create_linkedList()
    - 연결리스트 객체 생성

    """
    __head = None

    def __init__(self):
        self.__head = Node(None)









