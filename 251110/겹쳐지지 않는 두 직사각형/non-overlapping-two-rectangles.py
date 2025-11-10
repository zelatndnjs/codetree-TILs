N, M = map(int,input().split())
cube = [list(map(int, input().split())) for i in range(N)]

def area(cube, x1, y1, x2, y2):
    return sum(sum(cube[i][y1:y2+1]) for i in range(x1, x2+1))

def iscol(x1,y1, x2, y2, a1,b1,a2,b2):
    if max(x1,x2) < min(a1,a2) or max(a1,a2) < min(x1,x2):
        return True
    elif max(y1,y2) < min(b1,b2) or max(y1,y2) < min(b1,b2):
        return True
    else:
        return False

answer = -200000
for x1 in range(N):
    for x2 in range(x1, N):
        for y1 in range(M):
            for y2 in range(y1,M):
                for a1 in range(N):
                    for a2 in range(a1, N):
                        for b1 in range(M):
                            for b2 in range(b1, M):
                                if iscol(x1,y1, x2, y2, a1,b1,a2,b2):
                                    answer = max(answer, area(cube,x1,y1,x2,y2) + area(cube,a1,b1,a2,b2))


print(answer)
