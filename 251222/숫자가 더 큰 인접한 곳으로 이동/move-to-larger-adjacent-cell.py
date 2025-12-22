n,x,y = map(int, input().split())
x-= 1
y-= 1
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0,0, -1, 1]

answer = []
answer.append(grid[x][y])
def real(x,y,n):
    return x>=0 and x<n and y>=0 and y< n

while True:
    chk = 0
    for i in range(4):
        if real(x+dx[i], y+dy[i],n):
            if grid[x+dx[i]][y+dy[i]] > grid[x][y]:
                answer.append(grid[x+dx[i]][y+dy[i]])
                x = x+dx[i]
                y = y+dy[i]
                chk = 1
                break
    if chk ==0:
        break

for i in answer:
    print(i, end=' ')