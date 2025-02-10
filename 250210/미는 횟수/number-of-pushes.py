chk = 0
A = input()
ran = len(A)
B = input()
cnt = 0
for i in range(ran):
    if A == B:
        chk = 1
        break
    else:
        A = A[-1] + A[:-1:]
        cnt += 1
if chk == 0:
    print(-1)
else:
    print(cnt)