N = int(input())
cube = [list(map(int, input().split())) for i in range(N)]
nums = []
def find(cube, x, y,a,b, N, r, num, nums):
    num += cube[x][y]
    if r == 1:
        if x < N -1 and y > 0:
            find(cube,x+1, y-1, a,b,N, r, num, nums)
        if x < N - 1 and y < N - 1:
            find(cube,x+1, y+1, a,b,N, r+1, num, nums)
    elif r == 2:
        if x < N - 1 and y < N - 1:
            find(cube, x + 1, y + 1, a, b, N, r, num, nums)
        if x > 0 and y < N - 1:
            find(cube, x-1, y+1, a,b,N, r+1, num, nums)
    elif r == 3:
        if x > 0 and y < N - 1:
            find(cube, x - 1, y + 1, a, b, N, r, num, nums)
        if x>0 and y >0:
            find(cube, x-1, y-1, a,b,N,r+1,num, nums)
    else:
        if x == a and y == b:
            num -= cube[x][y]
            nums.append(num)
        else:
            if x>0 and y>0:
                find(cube, x - 1, y - 1, a, b, N, r, num, nums)
            else:
                pass
for i in range(N):
    for j in range(N):
        find(cube,i,j,i,j,N,1, 0,nums)

print(max(nums))
