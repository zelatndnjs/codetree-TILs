n,m,q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def move(arr, d):
    if d == 'L':
        arr = [arr[-1]] + arr[:-1:]
    else:
        arr = arr[1::] + [arr[0]]
    return arr

def chk(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            return True
    return False

def upwind(grid, r, d):
    grid[r] = move(grid[r], d)
    if d == 'L':
        d = 'R'
    else:
        d = 'L'
    if r > 0:
        if chk(grid[r-1], grid[r]):
            upwind(grid, r-1, d)

def downwind(grid, r, d):
    grid[r] = move(grid[r], d)
    if d == 'L':
        d = 'R'
    else:
        d = 'L'
    if r < len(grid) - 1:
        if chk(grid[r+1], grid[r]):
            downwind(grid, r+1, d)


for i in range(q):
    r,d = input().split()
    r = int(r)
    r -= 1
    upwind(grid, r, d)
    if d == 'L':
        d = 'R'
    else:
        d = 'L'
    if r < len(grid) - 1:
        if chk(grid[r], grid[r+1]):
            downwind(grid, r+1, d)

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()