a,b= map(int,input().split())
l = []
l.append(a)
l.append(b)
print(f"{sum(l)} {sum(l)/len(l):.1f}")