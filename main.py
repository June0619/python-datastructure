from my_collections.stack import Stack
from my_collections.queue import Queue

def test_stack():
    # Stack Test
    # 객체 인스턴스 할당 및 최대 저장공간 지정
    stack = Stack(2)

    # push test
    stack.push('A')
    stack.push('B')
    stack.push('C')

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


def test_queue():
    # Queue 테스트
    queue = Queue(4)

    queue.add('A')
    queue.add('B')
    queue.add('C')
    queue.add('D')
    queue.add('E')
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
    queue.add('A')
    queue.add('B')
    queue.add('C')
    queue.add('D')
    print(queue.delete())
    queue.add('E')
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())
    print(queue.delete())


if __name__ == '__main__':
    # test_queue()

    obj = Stack(5)
    for i in range(3):
        obj.push(i)

    print(obj[0])



