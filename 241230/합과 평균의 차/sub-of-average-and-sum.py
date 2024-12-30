a,b,c= map(int,input().split())
l = []
l.append(a)
l.append(b)
l.append(c)
print(f"{sum(l)}\n{sum(l)//len(l)}\n{sum(l)-sum(l)//len(l)}")