n, num = map(int, input().split())
arr = list(map(int, input().split()))
cnt = []
a = 0
for i in arr:
    if i > num:
        a += 1
    else:
        cnt.append(a)
        a = 0
cnt.append(a)
print(max(cnt))
