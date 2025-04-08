n,m = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
square = [[0 for i in range(m)]for j in range(n)]
d = 0
def insquare(square, x, y):
    if x>=0 and x<n and y>=0 and y<m:
        if square[x][y]==0:
            return True
        else:
            return False
    else:
        return False
x = 0
y = 0
num = 0
for i in range(n*m):
    num += 1
    square[x][y] = num
    if insquare(square, x+dx[d], y+dy[d]):
        x = x+dx[d]
        y = y+dy[d]
    else:
        d += 1
        d = d % 4
        x = x+dx[d]
        y = y+dy[d]
for x in range(n):
    for y in range(m):
        print(square[x][y], end=' ')
    print()