n = int(input())
grid = [[0 for _ in range(n+2)]]
for i in range(n):
    arr = list(map(int, input().split()))
    arr.insert(0,0)
    arr.append(0)
    grid.append(arr)
grid.append([0 for _ in range(n+2)])

# 1 = / 2 = \

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] # 0 = 상 1 = 우 2 = 하 3 = 좌

# 1일 때 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2
# 2일 때 0 -> 3, 3 -> 0, 1 -> 2, 2 -> 1

def isin(n,x,y):
    return 1 <= x < n+1 and 1 <= y < n+1

answer = []
t = 0


d = 0
sx = n + 1
for sy in range(1, n+2):
    x = sx
    y = sy
    x += dx[d]
    y += dy[d]
    t += 1
    while True:
        if not isin(n,x,y):
            break
        else:
            if grid[x][y] == 0:
                x += dx[d]
                y += dy[d]
                t += 1
            elif grid[x][y] == 1:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                else:
                    d = 2
                x += dx[d]
                y += dy[d]
                t += 1
            else:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                else:
                    d = 0
                x += dx[d]
                y += dy[d]
                t += 1
    answer.append(t)
    t=0
    d = 0
    sx = n + 1

d = 1
sy = 0
for sx in range(1, n+2):
    x = sx
    y = sy
    x += dx[d]
    y += dy[d]
    t += 1
    while True:
        if not isin(n,x,y):
            break
        else:
            if grid[x][y] == 0:
                x += dx[d]
                y += dy[d]
                t += 1
            elif grid[x][y] == 1:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                else:
                    d = 2
                x += dx[d]
                y += dy[d]
                t += 1
            else:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                else:
                    d = 0
                x += dx[d]
                y += dy[d]
                t += 1
    answer.append(t)
    t=0
    d = 1
    sy = 0

d = 2
sx = 0
for sy in range(1, n+2):
    x = sx
    y = sy
    x += dx[d]
    y += dy[d]
    t += 1
    while True:
        if not isin(n,x,y):
            break
        else:
            if grid[x][y] == 0:
                x += dx[d]
                y += dy[d]
                t += 1
            elif grid[x][y] == 1:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                else:
                    d = 2
                x += dx[d]
                y += dy[d]
                t += 1
            else:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                else:
                    d = 0
                x += dx[d]
                y += dy[d]
                t += 1
    answer.append(t)
    t=0
    d = 2
    sx = 0

d = 3
sy = n + 1
for sx in range(1, n+2):
    x = sx
    y = sy
    x += dx[d]
    y += dy[d]
    t += 1
    while True:
        if not isin(n,x,y):
            break
        else:
            if grid[x][y] == 0:
                x += dx[d]
                y += dy[d]
                t += 1
            elif grid[x][y] == 1:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                else:
                    d = 2
                x += dx[d]
                y += dy[d]
                t += 1
            else:
                if d == 0:
                    d = 3
                elif d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                else:
                    d = 0
                x += dx[d]
                y += dy[d]
                t += 1
    answer.append(t)
    t=0
    d = 3
    sy = n + 1

print(max(answer))