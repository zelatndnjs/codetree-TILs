n,k = map(int, input().split())
num = list(map(int, input().split()))
m = max(num)
def move(num, k, j, m):
    for i in range(j+1,j+k+1):
        if num[i] <= m:
            return i
    return -1
ans = 0
for i in range(m,0,-1):
    cur = 0
    chk = 0
    while True:
        if cur == -1:
            chk = 1
            break
        cur = move(num,k,cur,i)
        if cur == n-1:
            break
    if chk == 1:
        ans = i+1
        break
print(ans)