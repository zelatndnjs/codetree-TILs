cnt = 0
for i in range(4):
    l = list(map(int, input().split()))
    for j in l:
        if j%5==0:
            cnt += 1
print(cnt)