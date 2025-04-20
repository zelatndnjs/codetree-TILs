N, M = map(int, input().split())
c = [list(input()) for _ in range(N)]
def isIn(x, y, N, M):
    if x>=0 and x<N and y>=0 and y<M:
        return True
    else:
        return False

dxs = [0,-1, -1, -1, 0, 1, 1, 1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]

cnt = 0
for i in range(N):
    for j in range(M):
        if c[i][j] == 'L':
            for dx, dy in zip(dxs, dys):
                if isIn(i+dx, j+dy, N, M) and isIn(i+2*dx, j+2*dy, N, M):
                    if c[i+dx][j+dy] == 'E' and c[i+2*dx][j+2*dy] == 'E':
                        cnt += 1

print(cnt)