n, m = map(int, input().split())
num = list(map(int, input().split()))
ans = []
for start in range(n):
    s = 0
    startnum = num[start]
    for _ in range(m):
        s += startnum
        startnum = num[startnum-1]
    ans.append(s)
print(max(ans))

