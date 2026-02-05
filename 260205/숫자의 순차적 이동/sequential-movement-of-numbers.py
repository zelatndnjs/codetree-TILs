n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def isin(n,x,y):
    return 0<= x < n and 0 <= y < n

def move(n,x,y):
    global grid
    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,-1,-1,-1,0,1,1,1]
    newx = -1
    newy = -1
    big = -1
    for d in range(8):
        if isin(n, x+dx[d], y+dy[d]):
            if grid[x+dx[d]][y+dy[d]] > big:
                big = grid[x+dx[d]][y+dy[d]]
                newx = x+dx[d]
                newy = y+dy[d]
    tmp = grid[x][y]
    grid[x][y] = grid[newx][newy]
    grid[newx][newy] = tmp
for _ in range(m):
    for num in range(1,n*n+1):
        x = -1
        y = -1
        chk = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == num:
                    x = i
                    y = j
                    chk = 1
                    break
            if chk == 1:
                break
        move(n,x,y)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()