n = int(input())
num = list(map(int, input().split()))
ckdl = list()
for i in range(1, n):
    ckdl.append(num[i] - num[i - 1])
print(min(ckdl))