n = int(input())
num = list(map(int, input().split()))
profit = set()
profit.add(0)
for i in range(1,n):
    for j in range(i):
        profit.add(num[i]-num[j])
print(max(profit))