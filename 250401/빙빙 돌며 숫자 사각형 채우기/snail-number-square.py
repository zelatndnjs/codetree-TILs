n,m = map(int,input().split())
square = [[0 for i in range(m)] for _ in range(n)]
# 0 -> 1 아래 2 <- 3 up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def chk(square, x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    elif square[x][y] != 0:
        return False
    else:
        return True
x=0
y=0
num = 1
direction = 0
for i in range(n*m):
   square[x][y] = num
   num += 1
   newx = x+dx[direction]
   newy = y+dy[direction]
   if chk(square,newx,newy):
       x = newx
       y = newy
   else:
       direction += 1
       direction %= 4
       x = x+dx[direction]
       y = y+dy[direction]
for i in range(n):
    for j in range(m):
        print(square[i][j],end=" ")
    print()
