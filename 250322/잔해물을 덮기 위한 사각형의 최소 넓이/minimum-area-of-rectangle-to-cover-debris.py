plane = [[0 for _ in range(2001)] for _ in range(2001)]
offset = 1000
x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[0] += offset
y1[0] += offset
x2[0] += offset
y2[0] += offset
x1[1] += offset
y1[1] += offset
x2[1] += offset
y2[1] += offset
for i in range(x1[0], x2[0]+1):
    for j in range(y1[0], y2[0]+1):
        plane[i][j] = 1
for i in range(x1[1], x2[1]+1):
    for j in range(y1[1], y2[1]+1):
        plane[i][j] = 0
minx=0
miny=0
maxx=0
maxy=0
b = 0
for i in range(2000):
    if b == 1:
        break
    for j in range(2000):
        if plane[i][j] == 1:
            minx = i
            miny = j
            b = 1
            break

b = 0
for i in range(2000, -1, -1):
    if b == 1:
        break
    for j in range(2000, -1, -1):
        if plane[i][j] == 1:
            maxx = i
            maxy = j
            b = 1
            break
print((maxx- minx) * (maxy - miny))