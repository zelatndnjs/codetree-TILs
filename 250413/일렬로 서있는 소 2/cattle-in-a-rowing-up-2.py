n = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(len(A)- 2):
    for j in range(i+1,len(A)-1):
        for k in range(j+1,len(A)):
            if A[i] <= A[j] and A[j] <= A[k]:
                cnt += 1
print(cnt)