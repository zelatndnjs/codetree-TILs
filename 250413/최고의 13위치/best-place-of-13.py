n = int(input())
coin = [list(map(int, input().split())) for i in range(n)]
s = coin[0][0] + coin[0][1] + coin[0][2]
for x in range(0, n):
    for y in range(0, n-2):
        if coin[x][y] + coin[x][y+1] + coin[x][y+2] > s:
            s = coin[x][y] + coin[x][y+1] + coin[x][y+2]
print(s)