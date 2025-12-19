n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def chk(x, y, n):
    return x >= 0 and x < n and y >= 0 and y < n

def boom(grid, n, c):
    x = 0
    for i in range(n):
        if grid[i][c] != 0:
            x = i
            break
    y = c
    for i in range(grid[x][y]):
        if chk(x+i, y, n):
            grid[x+i][y] = 0
        if chk(x-i,y,n):
            grid[x-i][y] = 0
        if chk(x,y+i,n):
            grid[x][y+i] = 0
        if chk(x,y-i,n):
            grid[x][y-i] = 0

def arrange(grid, n):
    newgrid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        x = n-1
        for j in range(n-1,-1,-1):
            if grid[j][i] != 0:
                newgrid[x][i] = grid[j][i]
                x -= 1
    return newgrid


for _ in range(m):
    c = int(input())
    c -= 1
    boom(grid,n,c)
    grid = arrange(grid,n)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()