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

    * 편의상 연결리스트 내 데이터에 중복은 없다고 가정한다.
    """
    # Head 부분의 노드 Null 체크 생략용
    __head = Node("init")
    length = 0



