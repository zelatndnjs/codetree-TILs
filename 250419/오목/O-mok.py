square = [list(map(int, input().split())) for _ in range(19)]
def isWin(i,j,square, num):
    if square[i][j-1] == num and square[i][j-2] == num and square[i][j+1] == num and square[i][j+2] == num:
        return True
    elif square[i-1][j] == num and square[i-2][j] == num and square[i+1][j] == num and square[i+2][j] == num:
        return True
    elif square[i+1][j+1] == num and square[i+2][j+2] == num and square[i-1][j-1] == num and square[i-2][j-2] == num:
        return True
    elif square[i+1][j-1] == num and square[i+2][j-2] == num and square[i-1][j+1] == num and square[i-2][j+2] == num:
        return True
    else:
        return False
chk = 0
x = 0
y = 0
for i in range(2,17):
    for j in range(2,17):
        if square[i][j] == 1:
            if isWin(i,j,square, 1):
                x = i
                y = j
                chk = 1
        elif square[i][j] == 2:
            if isWin(i,j,square, 2):
                x = i
                y = j
                chk = 2
if chk == 1 or chk == 2:
    print(chk)
    print(x+1,y+1)
else:
    print(chk)
