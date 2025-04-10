n = int(input())
dx = [0,-1,0,1]
dy = [1,0,-1,0]
square = [[0 for i in range(n)]for j in range(n)]
d = 0
def insquare(square, x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False
x = n//2
y = n//2
num = 0
d = -1
for i in range(n*n):
    num += 1
    square[x][y] = num
    d += 1
    d = d % 4
    if insquare(square, x+dx[d], y+dy[d]):
        if square[x + dx[d]][y + dy[d]] != 0:
            d -= 1
            d = d % 4
        x = x+dx[d]
        y = y+dy[d]

for x in range(n):
    for y in range(n):
        print(square[x][y], end=' ')
    print()