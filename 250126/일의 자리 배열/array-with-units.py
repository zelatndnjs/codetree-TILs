a,b = map(int,input().split())
l = [a,b]
for i in range(8):
    l.append((l[-1]+l[-2])%10)
for i in l:
    print(i, end=' ')