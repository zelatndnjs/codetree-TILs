plane = [[0 for _ in range(201)] for _ in range(201)]
n = int(input())
area = 0
for i in range(n):
    x, y = map(int, input().split())
    x += 100
    y += 100
    for j in range(x, x+8):
        for k in range(y, y+8):
            if plane[j][k] == 0:
                plane[j][k] = 1
                area += 1
print(area)