n, m = map(int, input().split())
arr = [[0 for i in range(m)]for j in range(n)]

x=0
y=0

chk=0

startx=0
starty=0

for num in range(1, n*m+1):
    if x == m - 1:
        chk = 1
    if x==0 or y == n-1:
        arr[y][x] = num
        if chk == 0:
            startx += 1
            starty = 0
            x = startx
            y = starty
        else:
            starty += 1
            x = startx
            y = starty
    else:

        arr[y][x] = num
        x -= 1
        y += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()