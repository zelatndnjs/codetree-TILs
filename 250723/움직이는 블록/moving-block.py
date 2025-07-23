n = int(input())
blocks = [int(input()) for i in range(n)]
total = sum(blocks)
a = total // n
ans = 0
for i in blocks:
    if i > a:
        ans += i-a
print(ans)