t,a,b = map(int, input().split())
S = []
N = []
for i in range(t):
    alpa, num = input().split()
    num = int(num)
    if alpa == 'S':
        S.append(num)
    else:
        N.append(num)
S.sort()
N.sort()
cnt = 0
for i in range(a,b+1):
    distanceS = []
    distanceN = []
    for j in S:
        distanceS.append(abs(i-j))
    for j in N:
        distanceN.append(abs(i-j))
    if min(distanceS) <= min(distanceN):
        cnt += 1
print(cnt)