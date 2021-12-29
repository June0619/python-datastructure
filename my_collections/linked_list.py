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
    data = None
    next = None

    def __init__(self, p_data):
        self.data = p_data


class LinkedList:
    """
    1. LinkedList create_linkedList()
    - 연결리스트 객체 생성

    2. LinkedList add(data)
    - 연결리스트의 가장 마지막 노드에 새로운 데이터를 추가한다.
    """
    # Head 부분의 노드 Null 체크 생략용
    __head = Node("init")

    def append(self, data):
        """
        연결리스트의 마지막 노드에 새로운 데이터를 추가
        """
        last_link = self.__head

        # 노드의 링크 부분이 존재하지 않을때 까지 반복
        while last_link.next is not None:
            last_link = last_link.next

        last_link.next = Node(data)
        return self

    def __getitem__(self, key):
        """
        인덱스 값을 통해 접근
        연결리스트 특성상 모든 노드를 순차조회 해야 한다.
        """
        last_link = self.__head
        for _ in range(key):
            last_link = last_link.next
        return last_link.data
