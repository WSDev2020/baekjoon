from sys import stdin

data = None
deque = []

# 정수 X를 덱의 앞에 넣는다.
def push_front(val1):
    deque.insert(0, val1)

# 정수 X를 덱의 뒤에 넣는다.
def push_back(val1):
    deque.append(val1)

# 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop_front():
    if len(deque) <= 0:
        print(-1)
    else:
        p = deque.pop(0)
        print(p)

# 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop_back():
    if len(deque) <= 0:
        print(-1)
    else:
        p = deque.pop()
        print(p)

# 덱에 들어있는 정수의 개수를 출력한다.
def size():
    print(len(deque))

# 덱이 비어있으면 1을, 아니면 0을 출력한다.
def empty():
    print( 1 if len(deque) <= 0 else 0 )

# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def front():
    print(-1 if len(deque) <= 0 else deque[0])

# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def back():
    print(-1 if(len(deque) <= 0 ) else deque[(len(deque))-1])

for _ in range(int(stdin.readline())):
    data = stdin.readline().split()
    command = data[0]
    
    if(len(data) == 1):
        if(command == 'pop_front'):
            pop_front()
        elif(command == 'pop_back'):
            pop_back()
        elif(command == 'size'):
            size()
        elif(command == 'front'):
            front()
        elif(command == 'back'):
            back()
        elif(command == 'empty'):
            empty()
    else:
        number = data[1]
        if(command == 'push_front'):
            push_front(number)
        elif(command == 'push_back'):
            push_back(number)

