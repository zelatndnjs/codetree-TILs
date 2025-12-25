n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
k -= 1
top = []
for i in range(k, k+m):
    chk = 0
    for j in range(n-1):
        if grid[j][i] == 0 and grid[j+1][i] == 1:
            chk = 1
            top.append(j)
            break
    if chk == 0:
        top.append(n-1)

s = min(top)
for i in range(k,k+m):
    grid[s][i] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()