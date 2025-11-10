n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def chk(grid, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if grid[x][y] <= 0:
                return False
    return True


area = 0
for x1 in range(n):
    for x2 in range(x1,n):
        for y1 in range(m):
            for y2 in range(y1, m):
                if chk(grid, x1,y1,x2,y2):
                    area = max(area, (x2-x1+1)*(y2-y1+1))

print(area)