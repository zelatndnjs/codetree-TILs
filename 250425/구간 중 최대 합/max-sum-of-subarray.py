n, k = map(int, input().split())
num = list(map(int, input().split()))
max = num[0]
for i in range(n-k+1):
    a = 0
    for j in range(i, i+k):
        a += num[j]
    if max < a:
        max = a

print(max)


