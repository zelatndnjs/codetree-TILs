plane = [[0 for _ in range(2001)] for _ in range(2001)]

x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

for i in x1:
    i += 1000
for i in y1:
    i += 1000
for i in x2:
    i += 1000
for i in y2:
    i += 1000

area = 0

for i in range(x1[0], x2[0]):
    for j in range(y1[0], y2[0]):
        plane[i][j] = 1
        area += 1

for i in range(x1[1], x2[1]):
    for j in range(y1[1], y2[1]):
        if plane[i][j] == 0:
            area += 1
            plane[i][j] = 1

for i in range(x1[2], x2[2]):
    for j in range(y1[2], y2[2]):
        if plane[i][j] == 1:
            area -= 1
            plane[i][j] = 0
print(area)



