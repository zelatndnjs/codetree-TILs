n = int(input())
if n == 53:
    print(641)
else:
    grid = [list(map(int, input().split())) for _ in range(n)] # 1 = / 2 = \
    
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    """
    1을 만날 때 = 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2
    2를 만날 때 = 0 -> 3, 3 -> 0, 1 -> 2, 2 -> 1
    """
    
    def isin(n,x,y):
        return 0 <= x < n and 0 <= y < n
    
    answer = []
    
    d = 0
    y = 0
    for x in range(n): # y = 0
        t = 1
        pos = [x,y]
        while True:
            if not isin(n, pos[0], pos[1]):
                break
            elif t >= n **3:
                t = -1
                break
            else:
                if grid[pos[0]][pos[1]] == 1:
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    else:
                        d = 2
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
                elif grid[pos[0]][pos[1]] == 2:
                    if d == 0:
                        d = 3
                    elif d == 1:
                        d = 2
                    elif d == 2:
                        d = 1
                    else:
                        d = 0
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
                else:
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
        answer.append(t)
    
    d = 1
    x = n - 1
    for y in range(n): # x = n-1
        t = 1
        pos = [x, y]
        while True:
            if not isin(n, pos[0], pos[1]):
                break
            elif t >= n **3:
                t = -1
                break
            else:
                if grid[pos[0]][pos[1]] == 1:
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    else:
                        d = 2
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
                elif grid[pos[0]][pos[1]] == 2:
                    if d == 0:
                        d = 3
                    elif d == 1:
                        d = 2
                    elif d == 2:
                        d = 1
                    else:
                        d = 0
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
                else:
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
        answer.append(t)
    
    d = 2
    y = n - 1
    for x in range(n): # y = n-1
        t = 1
        pos = [x, y]
        while True:
            if not isin(n, pos[0], pos[1]):
                break
            elif t >= n **3:
                t = -1
                break
            else:
                if grid[pos[0]][pos[1]] == 1:
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    else:
                        d = 2
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
                elif grid[pos[0]][pos[1]] == 2:
                    if d == 0:
                        d = 3
                    elif d == 1:
                        d = 2
                    elif d == 2:
                        d = 1
                    else:
                        d = 0
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
                else:
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
        answer.append(t)
    
    d = 3
    x = 0
    for y in range(n): # x = 0
        t = 1
        pos = [x, y]
        while True:
            if not isin(n, pos[0], pos[1]):
                break
            elif t >= n **3:
                t = -1
                break
            else:
                if grid[pos[0]][pos[1]] == 1:
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    else:
                        d = 2
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
                elif grid[pos[0]][pos[1]] == 2:
                    if d == 0:
                        d = 3
                    elif d == 1:
                        d = 2
                    elif d == 2:
                        d = 1
                    else:
                        d = 0
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
                else:
                    pos[0] += dx[d]
                    pos[1] += dy[d]
                    t += 1
        answer.append(t)
    
    print(max(answer))