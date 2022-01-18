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

    def __init__(self, p_data):
        self.data = p_data

class DoublyCircularLinkedList:
    """
    연결리스트에서 마지막 노드와 첫번째노드가 서로 연결되어 있고, 데이터가 선행 노드와 후행 노드를 모두 바라보게 양방향으로 이동 가능하도록
    개선한 연결리스트

    1. DoublyCircularLinkedList create_doubly_circular_linked_list()
    - 이중 원형 연결 리스트 객체 생성

    2. DoublyCircularLinkedList add(data)
    - 연결리스트의 가장 마지막 노드에 새로운 데이터를 추가한다.

    3. DoublyCircularLinkedList insert(data)
    - 연결리스트의 특정 인덱스 번호 뒤에 데이터를 삽입한다.

    4. data [](index)
    - 연결리스트의 특정 인덱스의 값을 반환한다.

    * 편의상 연결리스트 내 데이터에 중복은 없다고 가정한다.
    """

    __head = None
    __tail = None
    length = 0

    # Head 노드의 Null 체크 분기를 생략하기 위해 임의의 init 노드를 할당한다.
    def __init__(self):
        self.__head = Node("init")

    def append(self, data):
        """
        연결리스트의 마지막 노드에 새로운 데이터를 추가
        :param data:
        :return self:
        """
        last_link = self.__head

        # 노드의 링크 부분이 헤드로 돌아가지 않을때까지 반복
        while last_link.next is not None \
                and last_link.next is not self.__head:
            last_link = last_link.next

        # data insert
        new_node = Node(data)

        # link connection
        if self.length > 0:
            # prev
            new_node.prev = last_link
            self.__head.prev = new_node
            # next
            new_node.next = self.__head
        else:
            # prev
            new_node.prev = new_node
            # next
            new_node.next = new_node
            # head 교체
            self.__head = new_node

        # link
        last_link.next = new_node

        self.length += 1
        return self

    def to_string(self):
        """
        연결리스트 전체 item 출력
        :return:
        """
        last_link = self.__head

        data_list = []
        while last_link is not None \
                and last_link.next is not self.__head:
            data_list.append(str(last_link.data))
            last_link = last_link.next
        data_list.append(str(last_link.data))

        print("Linked List Data [", ', '.join(data_list), "]")

    def __getitem__(self, key):
        """
        인덱스 값을 통해 접근
        연결리스트 특성상 모든 노드를 순차조회 해야 한다.
        :param key:
        :return last_link:
        """
        last_link = self.__head

        for _ in range(key):
            last_link = last_link.next
        return last_link

