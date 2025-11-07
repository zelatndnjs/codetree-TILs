N,M = map(int, input().split())
cube = [[0 for i in range(100)]for j in range(100)]
startx=25
starty=25
realcube = [list(map(int, input().split())) for i in range(N)]
gold=0
for i in range(N):
    for j in range(N):
        cube[startx+i][starty+j] = realcube[i][j]
        if realcube[i][j]==1:
            gold+=1
maxk=0
while True:
    if maxk**2+(maxk+1)**2 > gold*M:
        maxk -= 1
        # print(maxk)
        break
    else:
        maxk+=1

def find(x,y,cube,k):
    gold = 0
    startx = x-k
    starty = y-k
    for i in range(2*k+1):
        for j in range(2*k+1):
            if abs(startx+i-x) + abs(starty+j-y) > k:
                # print(f"거리 초과 : {startx+i}, {starty+j}, {abs(startx+i-x) + abs(starty+j-y)}")
                continue
            else:
                # print(f"거리 안 : {startx + i}, {starty + j}, {abs(startx + i - x) + abs(starty + j - y)}")
                gold += cube[startx+i][starty+j]
    # print(f"{x-25}, {y-25}, {k} 일 때 금 개수 : {gold}")
    return gold


maxgold = 0

for k in range(maxk+1):
    for i in range(N):
        for j in range(N):
            gold = find(startx+i, starty+j, cube, k)
            if k**2+(k+1)**2 <= gold*M:
                maxgold = max(maxgold, gold)

print(maxgold)