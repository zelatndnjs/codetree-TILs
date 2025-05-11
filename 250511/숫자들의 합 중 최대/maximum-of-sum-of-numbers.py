X, Y = map(int, input().split())
m=0
for i in range(X, Y+1):
    num = str(i)
    s=0
    for j in num:
        s += int(j)
    if m < s:
        m = s
print(m)
