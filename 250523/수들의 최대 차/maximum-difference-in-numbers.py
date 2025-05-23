n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]
small = min(num)
big = max(num)
ans = 0
for i in range(small, big):
    cnt = 0
    for j in num:
        if j >= i and j <= i+k:
            cnt += 1
    ans = max(cnt, ans)
print(ans)