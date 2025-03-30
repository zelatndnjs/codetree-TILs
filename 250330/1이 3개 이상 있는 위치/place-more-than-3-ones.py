def isin(n, x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False
n = int(input())
square = [list(map(int, input().split())) for i in range(n)]
dxs = [1,0,-1,0]
dys = [0,1,0,-1]
fullcount = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            if isin(n, i+dx, j+dy):
               if square[i+dx][j+dy] == 1:
                cnt += 1
        if cnt >= 3:
            fullcount += 1
print(fullcount)