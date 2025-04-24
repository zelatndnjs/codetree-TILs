n,s = map(int,input().split())
num = list(map(int,input().split()))
sums = []
total = sum(num)
for i in range(n-1):
    for j in range(i+1, n):
        sums.append(abs(s - (total - num[i] - num[j])))
print(min(sums))