n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
k -= 1
top = []
for i in range(k, k+m):
    for j in range(n-1,-1,-1):
        if grid[j][i] == 0:
            top.append(j)
            break
s = min(top)
for i in range(k,k+m):
    grid[s][i] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()