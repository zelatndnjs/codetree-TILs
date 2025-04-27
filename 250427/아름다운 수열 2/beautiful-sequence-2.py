n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b = sorted(b)
cnt = 0
for i in range(n-m+1):
    if sorted(a[i:i+m]) == b:
        # print(sorted(a[i:i+m]))
        # print(b)
        cnt += 1
print(cnt)