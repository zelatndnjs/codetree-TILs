import sys

n,k = map(int, input().split())
num = list(map(int, input().split()))
minnum = min(num)
maxnum = max(num)

ans = sys.maxsize

for i in range(minnum, maxnum-k+1):
    # i ~ i + k
    cost = 0
    for j in num:
        if j >= i and j <= i+k:
            continue
        elif j < i:
            cost += i-j
        else:
            cost += j - (i+k)
    ans = min(ans, cost)
print(ans)