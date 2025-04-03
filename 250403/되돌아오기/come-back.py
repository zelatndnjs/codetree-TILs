n = int(input())
dxs = [1,0,-1,0]
dys = [0,1,0,-1]
x = 0
y = 0
chk = 0
cnt = 1
for i in range(n):
    direction, t = input().split()
    t = int(t)
    d = 0
    if direction == 'E':
        d = 1
    elif direction == 'W':
        d = 3
    elif direction == 'N':
        d = 2
    else:
        d = 0
    for j in range(t):
        x += dxs[d]
        y += dys[d]
        if chk ==0:
            if x == 0 and y == 0:
                chk = 1
            else:
                cnt += 1
if chk == 0:
    cnt = -1
print(cnt)