n = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if num[i] == 2:
        cnt += 1
        if cnt == 3:
            print(i+1)