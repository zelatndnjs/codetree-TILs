def interesting(a):
    num = list(str(a))
    total = len(num)
    num.sort()
    for i in range(total):
        if num[0] != num[1] and allSame(num[1:]) or num[-1] != num[-2] and allSame(num[:-1:]):
            return True
        else:
            return False
def allSame(n):
    chk = 0
    for i in range(len(n)-1):
        if n[i] != n[i+1]:
            chk = 1
            break
    if chk == 0:
        return True
    else:
        return False

x, y = map(int, input().split())
cnt = 0
for i in range(x,y+1):
    if interesting(i):
        cnt += 1
print(cnt)