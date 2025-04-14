r,c = map(int,input().split())
board = [list(input().split()) for _ in range(r)]
cnt = 0
if board[0][0] == 'W':
    for i in range(1,r-2):
        for j in range(1,c-2):
            if board[i][j] == 'B':
                for k in range(i+1, r-1):
                    for p in range(j+1, c-1):
                        if board[k][p] == 'W':
                            cnt += 1
else:
    for i in range(1,r-2):
        for j in range(1,c-2):
            if board[i][j] == 'W':
                for k in range(i+1, r-1):
                    for p in range(j+1, c-1):
                        if board[k][p] == 'B':
                            cnt += 1
print(cnt)