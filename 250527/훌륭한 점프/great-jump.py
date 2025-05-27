n,k = map(int, input().split())
num = list(map(int, input().split()))
m = max(num)
def move(num, cur, k, i):
    chk = 0
    if num[cur] <= i:
        for j in range(cur+1, min(n, cur+k+1)):
            if num[j] <= i:
                chk = 0
                return j
            else:
                chk = 1
        if chk == 1:
            return -1
        return -1
    else:
        return -1
ans = 0
for i in range(m,-1,-1):
    cur = 0
    chk = 0
    while True:
        if cur == -1:
            chk = 1
            break
        elif cur == n-1:
            break
        else:
            cur = move(num,cur,k,i)
    if chk == 1:
        ans = i+1
        break
print(ans)