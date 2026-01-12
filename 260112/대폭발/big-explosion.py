n,m,r,c = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
r -= 1
c -= 1

grid[r][c] = 1

def isin(x,y,n):
    return x >= 0 and x < n and y >= 0 and y < n

def boom(x,y,n,t, newgrid):
    t = 2**(t-1)
    if isin(x+t,y,n):
        newgrid[x+t][y] = 1
    if isin(x-t,y,n):
        newgrid[x-t][y] = 1
    if isin(x,y+t,n):
        newgrid[x][y+t] = 1
    if isin(x,y-t,n):
        newgrid[x][y-t] = 1
    return newgrid


for t in range(1, m+1):
    newgrid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                newgrid = boom(i,j,n,t, newgrid)

    for i in range(n):
        for j in range(n):
            if newgrid[i][j] == 1:
                grid[i][j] = 1

print(sum(sum(x) for x in grid))
