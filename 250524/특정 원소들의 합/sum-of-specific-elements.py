cnt = 0
for i in range(4):
    l = list(map(int, input().split()))
    for j in range(i+1):
        cnt += l[j]
print(cnt)