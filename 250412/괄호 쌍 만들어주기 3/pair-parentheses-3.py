A = input()
cnt = 0
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        if A[i] == '(':
            if A[j] == ')':
                cnt += 1
print(cnt)
