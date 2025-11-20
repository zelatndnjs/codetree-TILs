import math

n,m,q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
winds = [tuple(map(int, input().split())) for _ in range(q)]

def rotate(grid, r1,c1,r2,c2):
    r1 -= 1
    c1 -=1
    r2 -=1
    c2 -=1
    grid[r1].insert(c1, grid[r1+1][c1])
    tmp = grid[r1].pop(c2+1)
    for i in range(r1+1,r2+1):
        tmp2 = grid[i][c2]
        grid[i][c2] = tmp
        tmp = tmp2
    grid[r2].insert(c2, tmp)
    tmp = grid[r2].pop(c1)
    for i in range(r2-1, r1, -1):
        tmp2 = grid[i][c1]
        grid[i][c1] = tmp
        tmp = tmp2


for nothing in range(q):
    r1,c1,r2,c2 = winds[nothing]
    rotate(grid, r1,c1,r2,c2)
    # for x in range(n):
    #     for y in range(m):
    #         print(grid[x][y], end=' ')
    #     print()
    # print('-------------------------------')
    newgrid = [[0 for _ in range(m)] for _ in range(n)]
    for a in range(n):
        for b in range(m):
            newgrid[a][b] = grid[a][b]
    r1 -=1
    c1 -=1
    r2 -=1
    c2 -=1
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            rotn = 1
            gkq = newgrid[i][j]
            if i-1 >= 0:
                rotn += 1
                gkq += newgrid[i-1][j]
            if j - 1 >= 0:
                rotn += 1
                gkq += newgrid[i][j-1]
            if i+1 <= n-1:
                rotn += 1
                gkq += newgrid[i+1][j]
            if j+1 <= m-1:
                rotn += 1
                gkq += newgrid[i][j+1]
            grid[i][j] = math.trunc(gkq / rotn)
    # for x in range(n):
    #     for y in range(m):
    #         print(grid[x][y], end=' ')
    #     print()
    # print('-------------------------------')

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()