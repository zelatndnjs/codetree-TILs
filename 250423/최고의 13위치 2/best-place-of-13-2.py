n = int(input())
coins = [list(map(int, input().split())) for _ in range(n)]
cnt1 = 0
cnt2 = 0
s = 0
for i in range(n):
    for j in range(n-2):
        cnt1 = 0
        cnt1 = coins[i][j] + coins[i][j+1] + coins[i][j+2]
        for k in range(i,n):
            cnt2=0
            if k==i:
                for p in range(j+3, n-2):
                    cnt2 = coins[k][p] + coins[k][p+1] + coins[k][p+2]
                    if cnt1 + cnt2 > s:
                        s = cnt1+cnt2

            else:
                for p in range(n-2):
                    cnt2 = coins[k][p] + coins[k][p+1] + coins[k][p+2]
                    if cnt1 + cnt2 > s:
                        s = cnt1 + cnt2
            if cnt1 + cnt2 > s:
                s = cnt1+cnt2
print(s)