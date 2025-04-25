n, k = map(int, input().split())
num = [0 for _ in range(10001)]
alist = []
for i in range(n):
    a,b = input().split()
    a = int(a)
    alist.append(a)
    if b == 'G':
        num[a] = 1
    else:
        num[a] = 2
m = 0
for i in range(max(alist)-k):
    s = 0
    for j in range(i, i+k+1):
         s += num[j]
    if m < s:
        m = s
print(m)