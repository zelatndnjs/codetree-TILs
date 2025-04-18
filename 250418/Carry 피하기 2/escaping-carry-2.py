n = int(input())
def isCarry(a,b,c):
    l = max(len(a), len(b), len(c))
    a = a.zfill(l)[::-1]
    b = b.zfill(l)[::-1]
    c = c.zfill(l)[::-1]
    for i in range(l):
        if int(a[i])+int(b[i])+int(c[i]) >= 10:
            return True
    return False

num = [input() for _ in range(n)]

realnum = []
for i in range(len(num)-2):
    for j in range(i+1, len(num)-1):
        for k in range(j+1, len(num)):
            if isCarry(num[i],num[j],num[k]):
                continue
            else:
                realnum.append(int(num[i]) + int(num[j]) + int(num[k]))
print(max(realnum))