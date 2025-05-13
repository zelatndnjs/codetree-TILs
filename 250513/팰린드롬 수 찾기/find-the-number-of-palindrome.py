def isPal(n):
    a = list(str(n))
    for i in range(len(a)//2):
        if a[i] != a[len(a)-i-1]:
            return False
    return True

x,y = map(int,input().split())
cnt = 0
for i in range(x,y+1):
    if isPal(i):
        cnt += 1
print(cnt)