pp, p = map(int, input().split())
print(pp,p,end=' ')
for _ in range(8):
    pp,p = p, pp*2+p
    print(p,end=' ')