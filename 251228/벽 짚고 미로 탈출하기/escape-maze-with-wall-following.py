n = int(input())
x,y = map(int, input().split())
grid = [['!' for _ in range(n+2)] for _ in range(n+2)]
for i in range(1, n+1):
    str = input()
    for j in range(1, n+1):
        grid[i][j] = str[j-1]

answer = 0
sx = x
sy = y
d = 3 # 0 = 상 1= 하 2 = 좌 3 = 우

while True:
    if grid[x+1][y] == '#' and grid[x-1][y] == '#' and grid[x][y-1] == '#' and grid[x][y+1] == '#':
        answer = -1
        break
    elif grid[x+1][y] == '#' and grid[x][y+1] == '#' and grid[x-1][y] == '#':
        d = 2
    elif grid[x][y-1] == '#' and grid[x][y+1] == '#' and grid[x-1][y] == '#':
        d = 1
    elif grid[x][y-1] == '#' and grid[x-1][y] == '#' and grid[x+1][y] == '#':
        d = 3
    elif grid[x][y-1] == '#' and grid[x][y+1] == '#' and grid[x+1][y] == '#':
        d = 0
    elif grid[x+1][y] == '#' and grid[x-1][y] == '#':
        pass
    elif grid[x][y-1] == '#' and grid[x][y+1] == '#':
        pass
    elif grid[x+1][y] == '#'  and grid[x][y-1] == '#':
        if d == 1:
            d = 3
        else:
            d = 0
    elif grid[x+1][y] == '#' and grid[x][y+1] == '#':
        if d == 3:
            d = 0
        else:
            d = 2
    elif grid[x-1][y] == '#' and grid[x][y-1] == '#':
        if d == 0:
            d = 3
        else:
            d = 1
    elif grid[x-1][y] == '#' and grid[x][y+1] == '#':
        if d == 3:
            d = 1
        else:
            d = 2
    elif grid[x+1][y] == '#':
        d = 3
    elif grid[x-1][y] == '#':
        d = 2
    elif grid[x][y-1] == '#':
        d = 1
    elif grid[x][y+1] == '#':
        d = 0
    else:
        if grid[x+1][y+1] == '#':
            if d == 2:
                d = 1
            else:
                d = 3
        elif grid[x+1][y-1] == '#':
            if d == 3:
                d = 1
            else:
                d = 2
        elif grid[x-1][y+1] == '#':
            if d == 2:
                d = 0
            else:
                d= 3
        elif grid[x-1][y-1] == '#':
            if d == 3:
                d = 0
            else:
                d = 2
        else:
            answer = -1
            break
    if d == 0:
        x -= 1
    elif d == 1:
        x += 1
    elif d == 2:
        y -= 1
    else:
        y += 1

    answer += 1

    if grid[x][y] == '!':
        break

    if x == sx and y == sy:
        answer = -1
        break

print(answer)