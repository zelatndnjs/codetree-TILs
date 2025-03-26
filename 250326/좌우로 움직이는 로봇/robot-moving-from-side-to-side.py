n, m = map(int, input().split())
A = [0]
B = [0]
aplace = 0
bplace = 0
for i in range(n):
    t,d = input().split()
    t = int(t)
    if d == 'L':
        for j in range(t):
            aplace -= 1
            A.append(aplace)
    else:
        for j in range(t):
            aplace += 1
            A.append(aplace)
for i in range(m):
    t,d = input().split()
    t = int(t)
    if d == 'L':
        for j in range(t):
            bplace -= 1
            B.append(bplace)
    else:
        for j in range(t):
            bplace += 1
            B.append(bplace)
if len(A) > len(B):
    for i in range(len(A)-len(B)):
        B.append(bplace)
else:
    for i in range(len(B)-len(A)):
        A.append(aplace)
cnt=0
for i in range(1, len(A)):
    if A[i-1] != B[i-1] and A[i] == B[i]:
        cnt += 1
print(cnt)
