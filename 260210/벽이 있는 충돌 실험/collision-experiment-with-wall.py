t = int(input())

class ball:
    def __init__(self, x,y,d,n):
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
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        if self.isin(self.x+dx[self.d], self.y+dy[self.d]):
            self.x = self.x + dx[self.d]
            self.y = self.y + dy[self.d]
        else:
            self.switch()

def chk(balls):
    r = set()
    for i in range(len(balls)-1):
        for j in range(i+1, len(balls)):
            if balls[i].x == balls[j].x and balls[i].y == balls[j].y:
                r.add(i)
                r.add(j)

    r = sorted(r, reverse=True)
    for i in r:
        del balls[i]

for time in range(t):
    balls = []

    n,m = map(int, input().split())

    for i in range(m):
        x,y,d = input().split()
        x = int(x) - 1
        y = int(y) - 1
        newball = ball(x,y,d,n)
        balls.append(newball)

    for i in range(2*n):
        for b in balls:
            b.move()
        chk(balls)

    print(len(balls))

