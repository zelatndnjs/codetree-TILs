n = int(input())
pp = 1
p = n
print(pp, p, end=' ')
while True:
    pp, p = p, p+pp
    print(p, end=' ')
    if p>=100:
        break