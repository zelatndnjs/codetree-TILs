n, t = map(int, input().split())
command = input()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1] # L이 +1 R -1
square = [list(map(int, input().split())) for _ in range(n)]
x = n//2
y = n//2
d=0
cnt = square[x][y]
def insquare(n, x, y):
    return x>=0 and x<n and y>=0 and y<n
for i in command:
    if i == 'R':
        d -= 1
        d %= 4
    elif i == 'L':
        d += 1
        d %= 4
    else:
        if insquare(n, x+dx[d], y+dy[d]):
            x = x+dx[d]
            y = y+dy[d]
            cnt += square[x][y]
            # print("현재 위치", x,y, "숫자", square[x][y])
        else:
            continue

print(cnt)
