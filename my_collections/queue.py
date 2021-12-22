class Queue:
    """
    1. Queue Create_q(maxQueueSize)

        큐의 크기가 maxStackSize인 빈 큐를 생성하고 반환한다.

    2. Boolean IsFull_q(queue, maxQueueSize)

        큐에 저장되어있 자료의 갯수를 파악하여 저장공간이 남아 있는지 확인한다.

    3. Queue Add_q(queue, item)

        큐에 저장공간이 있다면 rear 영역에 item을 삽입한다.

    4. Boolean IsEmpty_q(queue)

        큐의 front 포인터와 rear 포인터가 같은 주소를 가르키고 있는지 확인한다.

    5. Element Delete_q(queue)

        큐가 비어있는지 확인한 뒤 비어있지 않다면 front 영역의 데이터를 삭제하고 반환한다.
    """

    # 큐의 Front 영역과 Rear 영역을 가르킬 포인터 변수
    __front = None
    __rear = None

    # 큐의 저장공간을 나타내는 객체 변수
    __node = None

    """
    최대 큐 사이즈를 지정할 변수
    외부에서 큐의 최대크기를 임의로 변경하면 로직에 문제가 생기기 때문에
    이 변수 또한 private 하게 선언해야 한다.
    """
    __max_queue_size = 0

    # 큐의 초기화 함수
    def __init__(self, max_queue_size_p):

        self.node = list()
        self.__max_queue_size = max_queue_size_p
        self.__front = 0
        self.__rear = 0

        # 큐의 크기로 지정 된 인자만큼 초기화
        for _ in range(max_queue_size_p):
            self.node.append(None)

    # 큐가 가득 찬 상태인지 확인하는 함수
    # 큐 안에 빈 공간이 없다면 True 를 리턴한다
    def is_full(self):
        for data in self.node:
            if data is None:
                return False
        else:
            print('This queue is Full')
            return True

    # 큐가 가득 차지 않았다면 Rear 영역에 아이템을 삽입하는 함수
    # 아이템을 삽입한 뒤 Rear 포인터는 한칸 뒤로 이동한다.
    # 해당 큐는 원형큐이기 때문에 Rear 포인터는 순환하며 이동한다.
    def add(self, item):
        if self.is_full():
            return
        else:
            self.node[self.__rear] = item
            self.__rear = (self.__rear + 1) % self.__max_queue_size
            # print('now rear : ', self.__rear)

    # 큐가 비어있는지 확인하는 함수
    # Front 포인터와 Rear 포인터가 같은 주소를 가리키고 있다면 비어있는 것으로 간주한다. -- > Error
    # 원형 큐이기 때문에 꽉 찬 상태에도 Front 포인터와 Rear 포인터가 같은 주소를 가리키고 있을 수 있다.
    # 따라서 저장된 데이터 갯수로 판단해야 함.
    def is_empty(self):
        for data in self.node:
            if data is not None:
                return False
        else:
            print('This queue is Empty')
            return True

    # 큐가 비어있지 않다면 가장 먼저 삽입 된 데이터 하나를 반환받는 함수
    # Front 영역의 데이터를 반환하고 큐에서 제거한다.
    # 해당 큐는 원형큐이기 때문에 Front 포인터는 순환하며 이동한다.
    def delete(self):
        if self.is_empty():
            return
        else:
            temp = self.node[self.__front]
            self.node[self.__front] = None
            self.__front = (self.__front + 1) % self.__max_queue_size
            # print('now front : ', self.__front)
            return temp
















