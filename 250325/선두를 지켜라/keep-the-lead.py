n,m = map(int,input().split())
A = []
B = []
aplace = 0
for i in range(n):
    v,t = map(int,input().split())
    for j in range(1, t+1):
        aplace += v
        A.append(aplace)
bplace = 0
for i in range(m):
    v, t = map(int, input().split())
    for j in range(1, t + 1):
        bplace += v
        B.append(bplace)
if len(A) >= len(B):
    for i in range(len(A) - len(B)):
        B.append(B[-1])
else:
    for i in range(len(B)- len(A)):
        A.append(A[-1])
chk = [] # A가 선두면 -1 B가 선두면 1
cnt = 0
for i in range(len(A)):
    if A[i] > B[i]:
        chk.append(-1)
    elif A[i] < B[i]:
        chk.append(1)
    else:
        continue

for i in range(1, len(chk)):
    if chk[i] * chk[i-1] < 0:
        cnt += 1

print(cnt)