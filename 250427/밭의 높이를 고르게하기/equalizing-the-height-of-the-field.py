n,h,t = map(int,input().split())
levels = list(map(int,input().split()))
money = []
for i in range(n-1):
    for j in range(i, n):
        if j-i+1 >=t:
            cost = 0
            for k in range(i,j+1):
                cost += abs(levels[k] - h)
            money.append(cost)
print(min(money))
