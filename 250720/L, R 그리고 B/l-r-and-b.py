square = [list(input()) for _ in range(10)]
bpos = [0,0]
rpos = [0,0]
lpos = [0,0]
for i in range(10):
    for j in range(10):
        if square[i][j] == 'B':
            bpos[0] = i
            bpos[1] = j
        elif square[i][j] == 'R':
            rpos[0] = i
            rpos[1] = j
        elif square[i][j] == 'L':
            lpos[0] = i
            lpos[1] = j
chk = 0
if bpos[0] == rpos[0] == lpos[0]:
    if bpos[1] < rpos[1] and rpos[1] < lpos[1]:
        chk = 1
    elif bpos[1] > rpos[1] and rpos[1] > lpos[1]:
        chk = 1
elif bpos[1] == rpos[1] == lpos[1]:
    if bpos[0] < rpos[0] and rpos[0] < lpos[0]:
        chk = 1
    elif bpos[0] > rpos[0] and rpos[0] > lpos[0]:
        chk = 1
if chk == 0:
    print(abs(lpos[0] - bpos[0]) + abs(lpos[1] - bpos[1]) -1)
else:
    print(abs(lpos[0] - bpos[0]) + abs(lpos[1] - bpos[1]) +1)