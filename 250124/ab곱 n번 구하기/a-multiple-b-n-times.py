n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    result = 1
    for j in range(a,b+1):
        result *= j
    print(result)