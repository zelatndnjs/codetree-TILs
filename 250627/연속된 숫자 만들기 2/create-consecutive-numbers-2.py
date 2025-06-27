a,b,c = map(int, input().split())
small = min(a,b,c)
big = max(a,b,c)
mid = a+b+c - small - big
if mid - small > 2 and big - mid > 2:
    print(2)
elif mid - small == 2:
    print(1)
elif big - mid == 2:
    print(1)
elif big - mid == 1 and mid - small == 1:
    print(0)
else:
    print(2)