n = int(input())
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += 2
        print(cnt, end=' ')
        if cnt == 8:
            cnt = 0
    print()