from collections import deque

n,m,k = map(int, input().split())
grid = [[0]*n for _ in range(n)]

for _ in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    grid[x][y] = 1

snake = deque()
snake.appendleft((0,0))

def isin(n,x,y):
    return 0 <= x < n and 0 <= y < n

def iscollape(snake, next_x, next_y):
    return (next_x, next_y) in snake

def move(grid, snake, d, n):

    direction = {'U': [-1,0], 'D': [1,0], 'L': [0,-1], 'R': [0,1]}
    next_x = snake[0][0] + direction[d][0]
    next_y = snake[0][1] + direction[d][1]

    if isin(n, next_x, next_y):
        if grid[next_x][next_y] == 1:
            grid[next_x][next_y] = 0
            if iscollape(snake, next_x, next_y):
                return False
            else:
                snake.appendleft((next_x, next_y))
                return True
        else:
            snake.pop()
            if iscollape(snake, next_x, next_y):
                return False
            else:
                snake.appendleft((next_x, next_y))
                return True
    else:
        return False

answer = 0
chk = 0
for _ in range(k):
    if chk == 1:
        break
    else:
        d, p= input().split()
        p = int(p)
        for _ in range(p):
            if move(grid,snake,d,n):
                answer += 1
            else:
                answer += 1
                chk = 1
                break

print(answer)