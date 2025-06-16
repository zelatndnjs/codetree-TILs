import sys

n = int(input())
h = [int(input()) for _ in range(n)]
minh = min(h)
maxh = max(h)
cost = sys.maxsize
chk = 0
for i in range(minh, maxh-17):
    cost1 = 0
    # i ~ i+17
    for j in h:
        if j < i:
            cost1 += (i-j) ** 2
        elif j > i + 17:
            cost1 += (j-(i+17)) ** 2
        else:
            continue
    if cost1 < cost:
        chk = 1
        cost = cost1
if chk == 0:
    cost = 0
print(cost)
