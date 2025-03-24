a,b = map(int,input().split())
arr = [a,b]
for i in range(8):
    arr.append((a+b)%10)
for i in arr:
    print(i, end=' ')