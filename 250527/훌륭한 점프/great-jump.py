n,k = map(int, input().split())
num = list(map(int, input().split()))
m = max(num)

def move(num,k,cur,i):
    for j in range(cur+1, cur+k+1):
        if num[j] <= i:
            return j
    return -1
ans = 0
for i in range(m,-1,-1):
    cur = 0
    seq = []
    chk = 0
    while True:
        if cur == n-1:
            seq.append(num[cur])
            ans = max(seq)
            break
        elif cur == -1:
            chk = 1
            break
        seq.append(num[cur])
        cur = move(num,k,cur,i)

    if chk == 1:
        break
    else:
        ans = i
print(ans)
