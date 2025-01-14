a,b = map(int,input().split())

l = []

for i in range(a,b+1):
    if i % 5 == 0 or i % 7 == 0 :
        l.append(i)

print(f"{sum(l)} {sum(l)/len(l):.1f}")