a,b = map(int,input().split())
while True:
    if a>b:
        break
    print(a, end=' ')
    if a%2==1:
        a *= 2
    else:
        a += 3
