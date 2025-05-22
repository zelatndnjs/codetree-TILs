n,m = map(int, input().split())
d = dict()
for i in range(m):
    a,b = map(int, input().split())
    small = min(a,b)
    big = max(a,b)
    c = (small, big)
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
print(max(list(d.values())))