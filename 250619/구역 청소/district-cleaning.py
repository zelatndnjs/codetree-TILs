a, b = map(int, input().split())
c, d = map(int, input().split())
if c >= b or a >= d:
    print(b-a+d-c)
else:
    print(max(a,b,c,d) - min(a,b,c,d))