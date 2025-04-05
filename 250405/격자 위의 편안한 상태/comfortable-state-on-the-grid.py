n,m = map(int,input().split())
tile = [[0 for _ in range(n)]for _ in range(n)]
dxs = [1,0, -1, 0]
dys = [0,1,0,-1]
for i in range(m):
    r,c = map(int,input().split())
    tile[r-1][c-1] = 1
    x = r-1
    y = c-1
    cnt = 0
    for dx, dy in zip(dxs, dys):
        if x+dx >= 0 and x+dx < n and y+dy >= 0 and y+dy < n:
            if tile[x+dx][y+dy] == 1:
                cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)