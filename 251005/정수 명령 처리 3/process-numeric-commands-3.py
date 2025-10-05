from collections import deque

dq = deque()

N = int(input())
for i in range(N):
    m = input()
    if 'push_front' in m:
        a,b = m.split()
        b = int(b)
        dq.appendleft(b)
    elif 'push_back' in m:
        a,b = m.split()
        b = int(b)
        dq.append(b)
    else:
        if 'pop_front' == m:
            print(dq.popleft())
        elif 'pop_back' == m:
            print(dq.pop())
        elif 'size' == m:
            print(len(dq))
        elif 'empty' ==m:
            if len(dq) == 0:
                print(1)
            else:
                print(0)
        elif 'front' == m:
            print(dq[0])
        elif 'back' ==m:
            print(dq[-1])