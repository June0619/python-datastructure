from stack import Stack

if __name__ == '__main__':

    '''
    Stack Test
    '''
    # 객체 인스턴스 할당 및 최대 저장공간 지정
    stack = Stack(2)

    # push test
    stack.push('A')
    stack.push('B')
    stack.push('C')

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

