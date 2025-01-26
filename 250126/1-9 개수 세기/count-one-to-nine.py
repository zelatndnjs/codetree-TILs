n = int(input())
cnt = [0 for i in range(9)]
num = list(map(int, input().split()))
for i in num:
    cnt[i-1] += 1
for i in cnt:
    print(i)