n = int(input())
pigeons = dict()
cnt = 0
for i in range(n):
    a,b = map(int, input().split())
    if a in pigeons:
        if pigeons[a] != b:
            cnt += 1
            pigeons[a] = b
    else:
        pigeons[a] = b
print(cnt)
        