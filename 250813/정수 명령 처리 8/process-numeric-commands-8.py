from collections import deque

dq = deque()
n = int(input())
for i in range(n):
    a = input()
    if a[-1] >= '0' and a[-1] <= '9':
        b,c = a.split()
        c = int(c)
        if b == 'push_front':
            dq.appendleft(c)
        elif b == 'push_back':
            dq.append(c)
    else:
        if a == 'pop_front':
            print(dq.popleft())
        elif a == 'pop_back':
            print(dq.pop())
        elif a == 'size':
            print(len(dq))
        elif a == 'empty':
            if len(dq) == 0:
                print(1)
            else:
                print(0)
        elif a == 'front':
            print(dq[0])
        elif a == 'back':
            print(dq[-1])
