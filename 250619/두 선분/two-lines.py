x1,x2,x3,x4 = map(int, input().split())
if x3 > x2 or x1 > x4:
    print("nonintersecting")
else:
    print("intersecting")