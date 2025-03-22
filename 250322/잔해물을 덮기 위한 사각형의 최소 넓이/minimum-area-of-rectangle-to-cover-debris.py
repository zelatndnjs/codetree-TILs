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
for i in range(x1[0], x2[0]):
    for j in range(y1[0], y2[0]):
        plane[i][j] = 1
for i in range(x1[1], x2[1]):
    for j in range(y1[1], y2[1]):
        if plane[i][j] == 1:
            plane[i][j] = 0
x = []
y = []
for i in range(2001):
    for j in range(2001):
      if plane[i][j] == 1:
        x.append(i)
        y.append(j)
if len(x) == 0 and len(y) == 0:
    print(0)
else:
    print((max(x)- min(x)+1) * (max(y) - min(y)+1))
