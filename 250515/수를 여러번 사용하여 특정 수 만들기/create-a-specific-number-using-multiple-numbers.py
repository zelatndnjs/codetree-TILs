a,b,c = map(int, input().split())
maxA = c//a
maxB = c//b
ans = 0
for i in range(maxA+1):
    for j in range(maxB+1):
        if a*i+b*j <= c:
            ans = max(ans, a*i+b*j)
print(ans)