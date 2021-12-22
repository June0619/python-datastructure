class Stack:

    """
    1. Stack CreateS(maxStackSize)

    스택의 크기가 maxStackSize인 빈 스택을 생성하고 반환한다.

    2. Boolean IsFull(stack, maxStackSize)

    스택이 가득 찼는지 여부를 확인하여 반환한다.

    3. Stack Push(stack, item)

    스택이 가득 차지 않았다면 최상단 메모리에 데이터를 삽입한다.

    4. Boolean IsEmpty(stack)

    스택에 자료가 하나도 존재하지 않는지 여부를 확인하여 반환한다.

    5. Element Pop(stack)

    스택이 비어있는지 확인한 뒤 그렇지 않다면 최상단의 자료를 꺼내 삭제하고 반환한다.
    """

    # 스택 메모리를 저장할 변수
    # 생성과 동시에 초기화 됨. 외부에서 접근하지 못하도록 private 하게 선언해야 함.
    # 멤버 변수 앞에 '__'를 붙이면 외부에서 접근할 수 없음
    __node = None

    # 스택 최상단 인덱스를 가르키는 함수
    # None 으로 선언할 시 증감연산자에서 에러가 나므로 -1로 선언
    top = -1

    # 스택 최대 저장공간
    max_stack_size = 0

    # 스택 객체 초기화와 동시에 선언
    def __init__(self, max_stack_size_p):
        self.__node = list()
        self.max_stack_size = max_stack_size_p

    # 스택이 가득 찼는지 확인하는 함수
    # 스택의 최상단의 주소가 가르키는 값이 스택의 메모리 최대값 주소와 일치할 때 is_full True 를 리턴한다.
    def is_full(self):
        if self.top == self.max_stack_size - 1:
            return True
        else:
            return False

    # 스택에 object 를 하나 밀어넣는 함수
    # 스택에 공간이 있다면 원소를 하나 추가하고 그렇지 않다면 반환함
    def push(self, item):
        if self.is_full():
            print('this stack is full')
        else:
            self.__node.append(item)
            self.top += 1
            return self

    # 스택에 자료가 존재하는지 확인하는 함수
    # 자료가 없다면 true 를 반환하고 그렇지 않다면 false 를 반환함
    def is_empty(self):
        if self.top < 0:
            return True
        else:
            return False

    # 스택 메모리 최상단 자료를 삭제하고 반환하는 함수
    # 스택이 비어있지 않다면 실행 가능
    def pop(self):
        if self.is_empty():
            print('this stack is empty')
        else:
            self.top -= 1
            return self.__node.pop()
