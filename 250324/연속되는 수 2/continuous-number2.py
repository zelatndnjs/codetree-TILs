cnt = []
n = int(input())
num = []
for i in range(n):
    a = int(input())
    num.append(a)
a = 1
for i in range(1, len(num)):
    if num[i] != num[i-1]:
        cnt.append(a)
        a = 1
    else:
        a += 1
print(max(cnt))
