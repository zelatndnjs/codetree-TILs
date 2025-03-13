n = int(input())
class Point:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.distance = abs(x) + abs(y)

points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append(Point(i+1, x, y))
points.sort(key=lambda p: (p.distance, p.num))
for i in points:
    print(i.num)