import copy

n = int(input())
originalgrid = [list(map(int, input().split())) for _ in range(n)]
answer = []

def chk(x,y,n):
    return x >= 0 and x < n and y >= 0 and y < n

def boom(grid, x, y, n, answer):
    newgrid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(grid[x][y]):
        if chk(x+i,y,n):
            grid[x+i][y] = 0
        if chk(x-i,y,n):
            grid[x-i][y] = 0
        if chk(x,y+i,n):
            grid[x][y+i] = 0
        if chk(x,y-i,n):
            grid[x][y-i] = 0
    for i in range(n):
        index = n-1
        for j in range(n-1,-1,-1):
            if grid[j][i] != 0:
                newgrid[index][i] = grid[j][i]
                index -= 1

    s = 0
    for i in range(n):
        for j in range(n-1):
            if newgrid[i][j] == newgrid[i][j+1] and newgrid[i][j] != 0:
                s += 1
            if newgrid[j][i] == newgrid[j+1][i] and newgrid[j][i] != 0:
                s += 1
    answer.append(s)

for i in range(n):
    for j in range(n):
        grid = copy.deepcopy(originalgrid)
        boom(grid,i,j,n,answer)

print(max(answer))