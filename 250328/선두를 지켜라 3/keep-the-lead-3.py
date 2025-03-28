n,m = map(int, input().split())
A = []
aplace = 0
B = []
bplace = 0
for i in range(n):
    v,t = map(int, input().split())
    for j in range(t):
        aplace += v
        A.append(aplace)

for i in range(m):
    v,t = map(int, input().split())
    for j in range(t):
        bplace += v
        B.append(bplace)

if len(A) > len(B):
    for i in range(len(A)-len(B)):
        B.append(B[-1])
else:
    for i in range(len(B)-len(A)):
        A.append(A[-1])

chk = 0 # 1이면 A 2이면 B 3이면 A,B
cnt = 0
for i in range(len(A)):
    if A[i] > B[i]:
        newchk = 1
    elif A[i] < B[i]:
        newchk = 2
    else:
        newchk = 3
    if newchk != chk:
        cnt += 1
        chk = newchk
print(cnt)
