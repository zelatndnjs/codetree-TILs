start, end = map(int, input().split())
def a(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i ==0:
            cnt += 1
    return cnt
cnt = 0
for i in range(start, end+1):
    if a(i) == 3:
        cnt += 1
print(cnt)