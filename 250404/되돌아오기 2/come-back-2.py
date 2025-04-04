x =0
y=0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
d=1
cnt =0
chk =0
command = input()
for i in command:
    if i == 'L':
        d += 1
        d %= 4
        cnt +=1
    elif i == 'R':
        d -=1
        d %= 4
        cnt +=1
    else:
        x += dx[d]
        y += dy[d]
        cnt += 1
        if x == 0 and y == 0:
            chk = 1
            break
if chk == 0:
    print(-1)
else:
    print(cnt)

