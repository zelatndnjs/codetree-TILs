n,t = map(int,input().split())
r,c,d = input().split()
r = int(r)
r -= 1
c = int(c)
c -= 1
dxs = [0,-1,0,1]
dys = [1,0,-1,0]
direction = 0
if d == 'U':
    direction = 1
elif d == 'D':
    direction = 3
elif d == 'L':
    direction = 2
else:
    direction = 0
def change(direction):
    if direction == 0:
        direction = 2
    elif direction == 1:
        direction = 3
    elif direction == 2:
        direction = 0
    else:
        direction = 1
    return direction
for i in range(t):
    newr = r + dxs[direction]
    newc = c + dys[direction]
    if newr<0 or newr>=n or newc<0 or newc>=n:
        direction = change(direction)
    else:
        r = newr
        c = newc
print(r+1,c+1)