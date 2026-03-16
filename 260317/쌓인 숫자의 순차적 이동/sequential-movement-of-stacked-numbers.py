n,m = map(int, input().split())
grid = [[[0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        grid[i][j][0] = nums[j]
indexx = 0
indexy = 0
chk = 0
seq = list(map(int, input().split()))

def isin(n,x,y):
    return 0 <= x < n and 0 <= y < n

for s in seq:

    for i in range(n):
        for j in range(n):
            if s in grid[i][j]:
                indexx = i
                indexy = j
                chk = 1
                break
        if chk == 1:
            break
    chk = 0
    end = grid[indexx][indexy].index(s)
    bigx = -1
    bigy = -1
    bignum = -1
    for i in range(indexx-1, indexx+2):
        for j in range(indexy-1, indexy+2):
            if indexx != i or indexy != j:
                if isin(n,i,j):
                    if len(grid[i][j]) > 0:
                        for num in grid[i][j]:
                            if bignum < num:
                                bignum = num
                                bigx = i
                                bigy = j
    if bigx != - 1 and bigy != -1:
        new = grid[indexx][indexy][0:end+1]
        old = grid[indexx][indexy][end+1::]
        grid[indexx][indexy] = old
        grid[bigx][bigy] = new + grid[bigx][bigy]


for i in range(n):
    for j in range(n):
        if len(grid[i][j]) == 0:
            print("None")
        else:
            for s in grid[i][j]:
                print(s, end=' ')
            print()


