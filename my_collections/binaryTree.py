class Node:
    """
    트리의 노드
    """

    # 왼쪽 자식 노드
    left = None
    # 오른쪽 자식 노드
    right = None
    # 트리의 데이터
    data = None

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return "Data : {}".format(self.data)


class BinaryTree:
    """
    Simple Binary Tree
    1. init
    2. pre_order
    3. in_order
    4. post_order
    """

    # 트리의 루트 노드
    root = None

    # 트리의 초기화 함수
    def __init__(self):
        print("Generated TREE")

    def call_pre_order(self):
        self.pre_order(self.root)

    def pre_order(self, ptr):
        if ptr is not None:
            print(ptr.data)
            self.pre_order(ptr.left)
            self.pre_order(ptr.right)
        else:
            return






