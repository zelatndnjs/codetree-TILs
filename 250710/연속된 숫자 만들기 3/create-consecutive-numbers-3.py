a,b,c = map(int, input().split())
if b > (a+c) // 2: # c가 움직여야 됨
    print(b-(a+1))
else: # a가 움직여야 됨 1 2 6
    print(c-(b+1))