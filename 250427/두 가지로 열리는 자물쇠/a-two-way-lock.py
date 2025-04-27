n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def chk(i,j,k,a,b,c):
    if onechk(i,a) and onechk(j,b) and onechk(k,c):
        return True
    else:
        return False

def onechk(i,a):
    big = max(i,a)
    small = min(i,a)
    if big-small <= 2:
        return True
    elif small+n-big <= 2:
        return True
    else:
        return False
cnt = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if chk(i,j,k,a1,b1,c1) or chk(i,j,k,a2,b2,c2):
                cnt += 1
print(cnt)