a, b = map(int, input().split())
big = max(a, b)
small = min(a, b)
for i in range(big, small-1, -1):
    print(i,end=' ')