n = int(input())
num = list(map(int, input().split()))
num.sort()
a = num[:n:]
b = num[n::]
dif = []
for i in range(n):
    dif.append(b[i] - a[i])
print(min(dif))