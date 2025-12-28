n = int(input())
x,y = map(int, input().split())
grid = [['!' for _ in range(n+2)] for _ in range(n+2)]
for i in range(1, n+1):
    str = input()
    for j in range(1, n+1):
        grid[i][j] = str[j-1]

answer = 0
dx = [-1, 1, 0,0]
dy = [0,0, -1, 1]
sx = x
sy = y
d = 3 # 0 = 상 1= 하 2 = 좌 3 = 우
c = 0
while True:
    c += 1
    if grid[x+dx[d]][y+dy[d]] == '#':
        if d == 0:
            d = 2
        elif d == 1:
            d = 3
        elif d == 2:
            d = 1
        else:
            d = 0
    if grid[x+dx[d]][y+dy[d]] == '!':
        answer += 1
        break
    else:
        if d == 0:
            if grid[x+dx[d]][y+dy[d]+1] == '#':
                pass
            else:
                answer += 1
                x -= 1
                d = 3
        elif d == 1:
            if grid[x+dx[d]][y+dy[d]-1] == '#':
                pass
            else:
                answer += 1
                x += 1
                d = 2
        elif d == 2:
            if grid[x+dx[d]-1][y+dy[d]] == '#':
                pass
            else:
                answer += 1
                y -= 1
                d = 0
        else:
            if grid[x+dx[d]+1][y+dy[d]] == '#':
                pass
            else:
                answer += 1
                y += 1
                d = 1
    answer += 1
    x = x+dx[d]
    y = y+dy[d]
    if c >= (n+2)**2:
        answer = -1
        break


print(answer)