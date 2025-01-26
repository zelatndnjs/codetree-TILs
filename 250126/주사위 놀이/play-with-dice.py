cnt = [0 for i in range(6)]
num = list(map(int, input().split()))
for i in num:
    cnt[i-1] += 1
a = 1
for i in cnt:
    print(a,'-',i)
    a+=1