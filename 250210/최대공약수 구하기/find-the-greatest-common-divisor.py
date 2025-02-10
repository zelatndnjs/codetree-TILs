def f(n,m):
    small = min(n,m)
    for i in range(small, 0, -1):
        if n%i==0 and m%i==0:
            return i

n,m = map(int,input().split())
print(f(n,m))