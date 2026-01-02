n = int(input())
x,y = map(int, input().split())
grid = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    str = input()
    for j in range(n):
        grid[i][j] = str[j]
x -= 1
y -= 1
cur = [x,y]

sx = x
sy = y

d = 0 # 0 = 우 1 = 상 2 = 좌 3 = 하
dx = [0,-1, 0, 1]
dy = [1,0, -1, 0]

def isin(cur):
    global n
    return cur[0] >= 0 and cur[0] < n and cur[1] >= 0 and cur[1] < n

answer = 0

while True:
    if not isin(cur) or answer == -1:
        break

    while True:
        if grid[cur[0] + dx[d]][cur[1] + dy[d]] == '#':
            d = (d+1)%4
        else:
            answer += 1
            cur[0] += dx[d]
            cur[1] += dy[d]
            if cur[0] == sx and cur[1] == sy and d == 0:
                answer = -1
            d = (d-1)%4
            break

print(answer)


# for i in range(n): # 출력
#     for j in range(n):
#         print(grid[i][j], end=' ')
#     print()