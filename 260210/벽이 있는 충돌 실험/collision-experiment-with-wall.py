t = int(input())

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

class Ball:
    def __init__(self, x, y, d, n):
        self.x = x
        self.y = y
        if d == 'L':
            self.d = 3
        elif d == 'R':
            self.d = 2
        elif d == 'U':
            self.d = 1
        else:
            self.d = 0
        self.n = n

    def isin(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def switch(self):
        if self.d == 0:
            self.d = 1
        elif self.d == 1:
            self.d = 0
        elif self.d == 2:
            self.d = 3
        else:
            self.d = 2

    def move(self):
        next_x = self.x + DX[self.d]
        next_y = self.y + DY[self.d]

        if self.isin(next_x, next_y):
            self.x = next_x
            self.y = next_y
        else:
            self.switch()

def remove_collisions(balls):
    position_count = {}
    for b in balls:
        key = (b.x, b.y)
        if key in position_count:
            position_count[key] += 1
        else:
            position_count[key] = 1

    survivors = []
    for b in balls:
        if position_count[(b.x, b.y)] == 1:
            survivors.append(b)
    return survivors

for _ in range(t):
    n, m = map(int, input().split())
    balls = []

    for _ in range(m):
        x, y, d = input().split()
        x = int(x) - 1
        y = int(y) - 1
        balls.append(Ball(x, y, d, n))

    for _ in range(2 * n):
        for b in balls:
            b.move()
        balls = remove_collisions(balls)

        if not balls:  # 더 없으면 조기 종료 가능
            break

    print(len(balls))