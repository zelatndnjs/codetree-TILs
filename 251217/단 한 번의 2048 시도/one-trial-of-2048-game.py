grid = [list(map(int, input().split())) for _ in range(4)]

d = input()

if d == 'L':
    newgrid = []
    for k in range(4):
        a = []
        for j in range(4):
            if grid[k][j] != 0:
                a.append(grid[k][j])
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                a[i] *= 2
                a[i+1] = 0
        b = []
        for i in range(len(a)):
            if a[i] != 0:
                b.append(a[i])
        for i in range(4-len(b)):
            b.append(0)
        newgrid.append(b)
    grid = newgrid
elif d == 'R':
    newgrid = []
    for k in range(4):
        a = []
        for j in range(4):
            if grid[k][j] != 0:
                a.append(grid[k][j])
        for i in range(len(a)-1,0,-1):
            if a[i] == a[i - 1]:
                a[i] *= 2
                a[i - 1] = 0
        b = []
        for i in range(len(a)):
            if a[i] != 0:
                b.append(a[i])
        for i in range(4 - len(b)):
            b.insert(0,0)
        newgrid.append(b)
    grid = newgrid
elif d == 'U':
    newgrid = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        index = 0
        for j in range(4):
            if grid[j][i] != 0:
                newgrid[index][i] = grid[j][i]
                index += 1
    for i in range(4):
        for j in range(3):
            if newgrid[j][i] == newgrid[j+1][i]:
                newgrid[j][i] *= 2
                newgrid[j+1][i] = 0
    newgrid2 = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        index = 0
        for j in range(4):
            if newgrid[j][i] != 0:
                newgrid2[index][i] = newgrid[j][i]
                index += 1
    grid = newgrid2
else:
    newgrid = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        index = 3
        for j in range(3,-1,-1):
            if grid[j][i] != 0:
                newgrid[index][i] = grid[j][i]
                index -= 1
    for i in range(4):
        for j in range(3,0,-1):
            if newgrid[j][i] == newgrid[j-1][i]:
                newgrid[j][i] *= 2
                newgrid[j-1][i] = 0
    newgrid2 = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        index = 3
        for j in range(3,-1,-1):
            if newgrid[j][i] != 0:
                newgrid2[index][i] = newgrid[j][i]
                index -= 1
    grid = newgrid2

for i in range(4):
    for j in range(4):
        print(grid[i][j], end=' ')
    print()