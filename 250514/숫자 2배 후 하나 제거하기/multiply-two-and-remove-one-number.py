n = int(input())
num = list(map(int, input().split()))
ans = []
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        doublenum = num[i]
        deletenum = num[j]
        num[i] *= 2
        del num[j]
        s = 0
        for k in range(n-2):
            s += abs(num[k] - num[k+1])
        ans.append(s)
        num.insert(j, deletenum)
        num[i] //= 2
print(min(ans))