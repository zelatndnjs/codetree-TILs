n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r,c = map(int, input().split())
r -= 1
c -= 1
num = grid[r][c]

def chk(r,c,n):
    return r >= 0 and r < n and c >= 0 and c <n

def boom(grid, r, c, num, n):
    grid[r][c] = 0
    for i in range(1, num):
        if chk(r-i,c,n):
            grid[r-i][c] = 0
    for i in range(1, num):
        if chk(r+i,c,n):
            grid[r+i][c] = 0
    for i in range(1, num):
        if chk(r,c-i,n):
            grid[r][c-i] = 0
    for i in range(1, num):
        if chk(r,c+i,n):
            grid[r][c+i] = 0

boom(grid,r,c,num,n)

newgrid = [[0 for _ in range(n)] for _ in range(n)]

x=n-1
y = 0
for j in range(n):
    for i in range(n-1, -1, -1):
        if grid[i][j] != 0:
            newgrid[x][y] = grid[i][j]
            x -= 1
    y += 1
    x = n -1

for i in range(n):
    for j in range(n):
        print(newgrid[i][j], end=' ')
    print()