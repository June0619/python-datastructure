class TNode:
    """
        트리의 노드
        """

    # 왼쪽 자식 노드
    left = None
    # 오른쪽 자식 노드
    right = None
    # 왼쪽 쓰레드
    left_t = None
    # 오른쪽 쓰레드
    right_t = None
    # 트리의 데이터
    data = None

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return "Data : {}".format(self.data)


class TreadTree:
    root = None

    def __init__(self):
        print("Generated Thread Tree")




