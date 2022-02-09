class TNode:
    """
        트리의 노드
        """

    # 왼쪽 자식 노드
    left = None
    # 오른쪽 자식 노드
    right = None
    # 스레드 플래그 변수
    is_flag = False
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




