n,m = map(int ,input().split())
num = list(map(int, input().split())) # 7 2 1 5 6 3
maxnum = max(num)
m = m -1
ans = 0
while True:
    chk = 0
    m1 = 0
    number = 0
    for i in range(len(num)):
        if number + num[i] > maxnum:
            m1 += 1
            number = num[i]
        else:
            number += num[i]
    if m1 > m:
        maxnum += 1
    else:
        ans = maxnum
        break
print(ans)