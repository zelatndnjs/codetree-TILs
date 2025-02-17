def f(a,b):
    big = max(a,b)
    small = min(a,b)
    big = big +25
    small = small*2
    if a>b:
        return big, small
    else:
        return small, big

a,b = map(int,input().split())
a,b = f(a,b)
print(a,b)