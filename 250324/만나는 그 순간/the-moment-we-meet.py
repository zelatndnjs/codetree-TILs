n,m = map(int,input().split())
A = []
place = 0
for i in range(n):
    d,t  = input().split()
    t = int(t)
    if d == 'L':
        for j in range(t):
            place -= 1
            A.append(place)
    else:
        for j in range(t):
            place += 1
            A.append(place)
B = []
place = 0
for i in range(m):
    d,t  = input().split()
    t = int(t)
    if d == 'L':
        for j in range(t):
            place -= 1
            B.append(place)
    else:
        for j in range(t):
            place += 1
            B.append(place)
result = -1
if len(A) > len(B):
    for i in range(len(A)- len(B)):
        B.append(B[-1])
else:
    for i in range(len(B)-len(A)):
        A.append(A[-1])
for i in range(len(A)):
    if A[i] == B[i]:
        result = i+1
        break
print(result)