n = int(input())
cnt = 10
for i in range(n):
    for j in range(n):
        cnt -= 1
        print(cnt, end='')
        if cnt == 1:
            cnt = 10
    print()