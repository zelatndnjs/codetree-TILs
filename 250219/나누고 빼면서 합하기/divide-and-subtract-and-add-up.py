n,m = map(int,input().split())
A = list(map(int,input().split()))
result = 0
while True:
    if m == 1:
        result += A[m-1]
        break
    elif m %2 ==0:
        result += A[m-1]
        m = m // 2
    else:
        result += A[m-1]
        m = m - 1
print(result)