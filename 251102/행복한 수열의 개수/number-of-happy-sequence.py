N, M = map(int, input().split())
cube = [list(map(int, input().split())) for i in range(N)]
happy = 0
for i in range(N):
    consarr = []
    cons=1
    for j in range(N-1):
        if cube[i][j] == cube[i][j+1]:
            cons += 1
        else:
            consarr.append(cons)
            cons = 1
    if max(consarr) >= M:
        happy += 1
for i in range(N):
    consarr = []
    cons=1
    for j in range(N-1):
        if cube[j][i] == cube[j+1][i]:
            cons+=1
        else:
            consarr.append(cons)
            cons=1
    if max(consarr)>=M:
        happy+=1
print(happy)
