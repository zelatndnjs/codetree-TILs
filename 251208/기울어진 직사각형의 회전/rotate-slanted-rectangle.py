n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
x,y,q,w,e,r,d = map(int, input().split())
x-=1
y-=1
def p(grid,n):

    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=' ')
        print()

if d ==0:
    num = grid[x][y]
    for i in range(r):
        grid[x][y] = grid[x-1][y-1]
        x -= 1
        y -= 1
    for i in range(e):
        grid[x][y] = grid[x-1][y+1]
        x -= 1
        y += 1
    for i in range(w):
        grid[x][y] = grid[x+1][y+1]
        x += 1
        y+= 1
    for i in range(q-1):
        grid[x][y] = grid[x+1][y-1]
        x += 1
        y -= 1
    grid[x][y] = num
else:
    num = grid[x][y]
    for i in range(q):
        grid[x][y] = grid[x-1][y+1]
        x -= 1
        y += 1

    for i in range(w):
        grid[x][y] = grid[x-1][y-1]
        x -= 1
        y -= 1

    for i in range(e):
        grid[x][y] = grid[x+1][y-1]
        x += 1
        y-= 1

    for i in range(r-1):
        grid[x][y] = grid[x+1][y+1]
        x += 1
        y += 1

    grid[x][y] = num

p(grid,n)