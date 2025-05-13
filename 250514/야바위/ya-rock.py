n = int(input())
r = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(1,4):
    num = i
    cnt = 0
    for j in r:
        a,b,c = j
        if num == a:
            num = b
        elif num == b:
            num = a
        if num == c:
           cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)