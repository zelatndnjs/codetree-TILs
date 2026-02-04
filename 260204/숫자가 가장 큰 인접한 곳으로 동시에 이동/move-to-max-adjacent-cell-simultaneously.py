n,m,t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
balls = [[0]*n for _ in range(n)]
ballplace = []
for i in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    balls[x][y] = 1
    ballplace.append((x,y))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
d = 0

def isin(n, x, y):
    return 0 <= x < n and 0 <= y < n

def move(grid, x,y,n):
    global dx
    global dy
    value = 0
    reald = 0
    for d in range(4):
        if isin(n, x+dx[d], y+dy[d]):
            if grid[x+dx[d]][y+dy[d]] > value:
                value = grid[x+dx[d]][y+dy[d]]
                reald = d
    return x+dx[reald], y+dy[reald]

for i in range(t):
    newballs = [[0]*n for _ in range(n)]
    for ballp in ballplace:
        x,y = ballp
        newx, newy = move(grid,x,y,n)
        newballs[newx][newy] += 1
    ballplace = []
    for x in range(n):
        for y in range(n):
            if newballs[x][y] >= 2:
                newballs[x][y] = 0
            elif newballs[x][y] == 1:
                ballplace.append((x,y))
    balls = newballs

print(sum(sum(x) for x in balls))

