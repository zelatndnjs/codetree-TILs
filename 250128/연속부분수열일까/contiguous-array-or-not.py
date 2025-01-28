n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
chk = 0
if B[0] in A:
    start = A.index(B[0])
    for i in range(n2):
        if A[start] == B[i]:
            start += 1
            continue
        else:
            chk = 1
            break
else:
    print("NO")

if chk == 0:
    print("YES")
else:
    print("NO")