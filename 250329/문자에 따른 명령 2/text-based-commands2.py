command = input()
dx = [1,0,-1,0]
dy = [0,1,0,-1]
x = 0
y = 0
d = 1
for i in command:
    if i == 'L':
        d += 1
        d = d % 4
    elif i == 'R':
        d -= 1
        d %= 4
    else:
        x += dx[d]
        y += dy[d]
print(x, y)