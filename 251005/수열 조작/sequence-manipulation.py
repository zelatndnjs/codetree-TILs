from collections import deque


n = int(input())
dq = deque([i for i in range(1,n+1)])
while True:
    if len(dq) == 1:
        break
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])