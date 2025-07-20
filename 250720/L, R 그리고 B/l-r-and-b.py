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
print(abs(bpos[0] - lpos[0]) + abs(bpos[1] - lpos[1]) -1)