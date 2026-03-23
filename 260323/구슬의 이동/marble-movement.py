n,m,t,k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
# grid안에 숫자가 아닌 리스트를 만들고 거기에 딕셔너리를 넣는게 좋아보인다. ball이라는 딕셔너리를 만드는 것이다.

dx = [1,0,-1,0] # 0 = 아래 1 = 우 2 = 위 3= 좌
dy = [0,1,0,-1]

balls = []

for i in range(m):
    r,c,d,v = input().split()
    r= int(r) -1
    c = int(c) -1
    v = int(v)
    if d == "D":
        d = 0
    elif d == "R":
        d = 1
    elif d == "U":
        d = 2
    else:
        d = 3
    newball = {'idx':i, 'r':r,'c':c,'d':d, 'v':v}
    balls.append(newball)
    grid[r][c].append(newball)

def deleteball(grid, balls):
    global n
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > k:
                r =len(grid[i][j]) - k
                grid[i][j].sort(key=lambda x: (x["v"], x["idx"]))
                deleteindex = set()
                for p in range(r):
                    deleteindex.add(grid[i][j][p]["idx"])
                grid[i][j] = grid[i][j][r:]
                balls = [ball for ball in balls if ball["idx"] not in deleteindex]
    return balls



def move(balls, n):
    newgrid = [[[] for _ in range(n)] for _ in range(n)]

    for ball in balls:
        for i in range(ball['v']):
            ball['r'] += dx[ball['d']]
            if not (0 <= ball['r'] < n):
                ball['d'] = (ball['d']+2) % 4
                ball['r'] += 2*dx[ball['d']]
            ball['c'] += dy[ball['d']]
            if not (0 <= ball['c'] < n):
                ball['d'] = (ball['d'] + 2) % 4
                ball['c'] += 2 * dy[ball['d']]
        newgrid[ball['r']][ball['c']].append(ball)

    balls = deleteball(newgrid, balls)
    return newgrid, balls

for i in range(t):
    grid, balls = move(balls, n)

print(sum(len(cell) for row in grid for cell in row))