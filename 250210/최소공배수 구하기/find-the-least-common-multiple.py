def f(n,m):
    big = max(n,m)
    while True:
        if big %n ==0 and big%m == 0:
            return big
            break
        else:
            big += 1

n,m = map(int,input().split())
print(f(n,m))