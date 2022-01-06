# Python-DataStructure Exercise

## 노트정리 목차
1. [자료구조란 무엇인가](/Note/1.%20자료구조란%20무엇인가/1강%20자료구조란%20무엇인가.md)
2. [배열](/Note/2.%20배열/2강%20배열.md)
3. [스택](/Note/3.%20스택/3강%20스택.md)
4. [큐](/Note/4.%20큐/4강%20큐.md)
5. [선택트리, 숲 이진트리 개수](/Note/10.%20선택트리,%20숲,%20이진트리%20개수/10강%20선택트리,%20숲,%20이진트리%20개수.md)

## 1. Stack
1.Stack 내부 메모리를 List로 선언 시 외부에서 리스트 객체 인덱스번호에 임의대로 접근하여 값을 조작할 수 있으면 안됨. 따라서 스택 객체 내부의 저장공간은 반드시 private 하게 선언 할 필요가 있음.

## 2. Queue
- 원형 큐 구현
    - 수업에서 원형 큐 까지 다루었으므로 그냥 원형 큐로 구현 했음
    - 일반 큐와는 다르게 큐가 비어있는 상태를 front 포인터와 rear 포인터가 만나는 경우로 설정하면 안됨

## 3. LinkedList
- 연결리스트 구현
    - 연결리스트에 새로운 노드를 추가할 때 마다 head link 부분이 비어있는지 체크하기 보다, head 영역에 더미 데이터 노드를 삽입하는 것이 이득일 듯