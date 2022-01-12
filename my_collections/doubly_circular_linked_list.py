class Node:
    """
    이중 원형 연결리스트 노드 (Data Unit)
    """
    # 데이터
    data = None
    # 이전 노드 링크
    prev = None
    # 다음 노드 링크
    next = None

    def __init__(self, p_data, p_prev):
        self.data = p_data
        self.prev = p_prev


class DoublyCircularLinkedList:
    """
    연결리스트에서 마지막 노드와 첫번째노드가 서로 연결되어 있고, 데이터가 선행 노드와 후행 노드를 모두 바라보게 양방향으로 이동 가능하도록
    개선한 연결리스트

    1. DoublyCircularLinkedList create_doubly_circular_linked_list()
    - 이중 원형 연결 리스트 객체 생성

    2. LinkedList add(data)
    - 연결리스트의 가장 마지막 노드에 새로운 데이터를 추가한다.

    3. LinkedList insert(data)
    - 연결리스트의 특정 인덱스 번호 뒤에 데이터를 삽입한다.

    4. data [](index)
    - 연결리스트의 특정 인덱스의 값을 반환한다.

    * 편의상 연결리스트 내 데이터에 중복은 없다고 가정한다.
    """
    # Head 부분의 노드 Null 체크 생략용
    __head = Node("init")
    length = 0

    def append(self, data):
        """
        연결리스트의 마지막 노드에 새로운 데이터를 추가
        :param data:
        :return self:
        """
        last_link = self.__head

        # 노드의 링크 부분이 존재하지 않을때 까지 반복
        while last_link.next is not None:
            last_link = last_link.next

        last_link.next = Node(data)
        self.length += 1
        return self

    def insert(self, index, data):
        """
        연결리스트의 특정 인덱스에 값을 삽입
        :param index:
        :param data:
        :return self:
        """
        last_link = self.__head

        for _ in range(index):
            last_link = last_link.next

        temp_node = last_link.next
        last_link.next = Node(data)
        last_link.next.next = temp_node

        self.length += 1
        return self

    def delete(self, index):
        """
        연결리스트 특정 인덱스의 노드를 삭제한다
        :param index:
        :return:
        """
        last_link = self.__head

        for _ in range(index):
            last_link = last_link.next

        # 삭제하려는 노드가 마지막이 아닌 경우
        if last_link.next.next is not None:
            temp = last_link.next.next
            print("Deleted : ", last_link.next.data)
            del last_link.next
            last_link.next = temp
        # 삭제하려는 노드가 마지막 노드인 경우
        else:
            del last_link.next
            last_link.next = None

        self.length -= 1

    def to_string(self):
        """
        연결리스트 전체 item 출력
        :return:
        """
        last_link = self.__head.next

        data_list = []
        while last_link is not None:
            data_list.append(str(last_link.data))
            last_link = last_link.next

        print("Linked List Data [", ', '.join(data_list), "]")

    def __getitem__(self, key):
        """
        인덱스 값을 통해 접근
        연결리스트 특성상 모든 노드를 순차조회 해야 한다.
        :param key:
        :return last_link.data:
        """
        last_link = self.__head
        # 헤드의 더미데이터 제외
        for _ in range(key+1):
            last_link = last_link.next
        return last_link.data

