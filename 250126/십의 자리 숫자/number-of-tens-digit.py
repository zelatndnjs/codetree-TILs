cnt = [0 for i in range(10)]
num = list(map(int, input().split()))
for i in num:
    if i == 0:
        break
    cnt[i//10] += 1
for i in range(1,10):
    print(f"{i} - {cnt[i]}")