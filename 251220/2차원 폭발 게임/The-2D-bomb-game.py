n,m,k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def boom(grid, n, m):
    for _ in range(10):
        chk = 0
        newgrid = [[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            count = 1
            start = 0
            end = n-1
            for j in range(n-1):
                if grid[j][i] == grid[j+1][i] and grid[j][i] != 0:
                    count += 1
                else:
                    if count >= m:
                        chk = 1
                        end = j
                        for k in range(start, end+1):
                            grid[k][i] = 0
                    start = j+1
                    count = 1
            if count >= m and m != 1:
                chk = 1
                end = n-1
                for k in range(start, end+1):
                    grid[k][i] = 0
            elif count >= m:
                end = n-1
                for k in range(start, end+1):
                    grid[k][i] = 0
        for i in range(n):
            index = n-1
            for j in range(n-1, -1, -1):
                if grid[j][i] != 0:
                    newgrid[index][i] = grid[j][i]
                    index -= 1
        if chk == 0:
            break
        else:
            grid = newgrid

    return newgrid

def rotate(grid, n):
    newgrid1 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newgrid1[i][j] = grid[n-1-j][i]
    newgrid2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        index = n-1
        for j in range(n-1, -1, -1):
            if newgrid1[j][i] != 0:
                newgrid2[index][i] = newgrid1[j][i]
                index -= 1
    return newgrid2

def p(grid,n):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=' ')
        print()

for _ in range(k):
    grid = boom(grid,n,m)
    grid = rotate(grid,n)
grid = boom(grid,n,m)
answer = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            answer += 1
print(answer)