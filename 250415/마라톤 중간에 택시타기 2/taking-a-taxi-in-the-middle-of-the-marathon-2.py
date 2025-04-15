n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

distance = []
for i in range(1,n-1):
    d = 0
    for j in range(1, n):
        if i == j:
            pass
        elif i+1 == j:
            d += abs(x[j] - x[j-2]) + abs(y[j] - y[j-2])
        else:
            d += abs(x[j] - x[j - 1]) + abs(y[j] - y[j - 1])
    distance.append(d)
print(min(distance))