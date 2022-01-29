class Node:
    """
    트리의 노드
    """

    # 왼쪽 자식 노드
    __l_link = None
    # 오른쪽 자식 노드
    __r_link = None
    # 트리의 데이터
    data = None

    def __init__(self, data, l_link=None, r_link=None):
        self.__l_link = l_link
        self.__r_link = r_link
        self.data = data

    def getData(self):
        return self.data


class BinaryTree:
    """
    - 해당 트리 객체는 삽입 및 조회연산을 단순화 하기 위해 완전 이진 트리를 기준으로 작성한다. (레벨의 모든 노드를 채우고, 왼쪽부터 삽입)
    - 데이터 입력시 특별한 정렬 알고리즘은 없는 것으로 한다.

    1. Tree Create()
    ::= 트리를 생성하고 루트 노드를 가리키는 포인터를 반환한다.

    2. Destroy(Tree)
    ::= 트리 객체가 점유중인 메모리를 반환한다.

    3. Tree Copy_Tree(Tree)
    ::= 트리를 복사하고 새로 생성한 트리의 루트 노드를 가리키는 포인터를 반환한다.

    4. Node Insert(n)
    ::= 트리에 노드 n을 삽입한다.

    5. Delete()
    ::= 트리에서 노드를 삭제한다. 보통 재구성 단계를 포함한다.

    6. Node Root()
    ::= 루트 노드 값을 반환한다.

    7. Node Parent(n)
    ::= 노드 n의 부모 노드를 반환한다. n이 루트노드이면 예외를 반환한다.

    8. List<Node> Children(n)
    ::= 노드 n의 자식 노드들을 반환한다. 노드 n이 리프노드이면 예외를 반환한다.

    9. boolean IsRoot(n)
    ::= 노드 n이 루트노드이면 True, 아니면 False를 반환한다.

    10. boolean IsInternal(n)
    ::= 노드 n이 내부노드이면 True, 아니면 False를 반환한다.

    11. boolean IsLeaf(n)
    ::= 노드 n이 리프노드이면 True, 아니면 False를 반환한다.

    12. boolean IsEmpty(Tree)
    ::= 트리가 비었으면 True, 아니면 False를 반환한다.

    13. Replace(n, m)
    ::= 노드 n을 노드 m으로 교체한다.
    """

    # 트리의 루트 노드
    __root = None

    # 트리의 초기화 함수
    def __init__(self):
        print("GENERATED TREE")

    def insert(self, data):
        new_node = Node(data)






