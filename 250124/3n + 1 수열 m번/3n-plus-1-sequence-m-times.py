m = int(input())
for _ in range(m):
    n = int(input())
    cnt = 0
    while True:
        if n ==1:
            break
        if n %2==0:
            n = n//2
        else:
            n = 3*n+1
        cnt += 1
    print(cnt)