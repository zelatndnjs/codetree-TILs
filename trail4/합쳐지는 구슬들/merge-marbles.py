class Ball:
    def __init__(self, r, c, d, w, n, num, chk):
        self.r = r
        self.c = c
        self.d = d
        self.w = w
        self.n = n
        self.num = num
        self.chk = chk

    def move(self):
        if self.d == 0:
            self.r -= 1
            if self.r < 0 or self.r >= n:
                self.r += 1
                self.d = 1
        elif self.d == 1:
            self.r += 1
            if self.r < 0 or self.r >= n:
                self.r -= 1
                self.d = 0
        elif self.d == 2:
            self.c -= 1
            if self.c < 0 or self.c >= n:
                self.c += 1
                self.d = 3
        else:
            self.c += 1
            if self.c < 0 or self.c >= n:
                self.c -= 1
                self.d = 2

def collapse(balls):
    new_balls = []
    for i in range(len(balls)):
        if balls[i].chk == 1:
            continue
        else:
            ball_group = []
            ball_group.append(balls[i])
            balls[i].chk = 1
            for j in range(i+1, len(balls)):
                if balls[j].chk == 1:
                    continue
                else:
                    if balls[i].r == balls[j].r and balls[i].c == balls[j].c:
                        ball_group.append(balls[j])
                        balls[j].chk = 1
            if len(ball_group) == 1:
                balls[i].chk = 0
                new_balls.append(balls[i])
            else:
                max_ball = max(ball_group, key=lambda ball : ball.num)
                total_weight = sum(ball.w for ball in ball_group)
                new_balls.append(Ball(max_ball.r, max_ball.c, max_ball.d, total_weight, max_ball.n, max_ball.num, 0))
    return new_balls


n,m,t = map(int, input().split())

balls = []

for num in range(m):
    r,c,d,w = input().split()
    r = int(r) - 1
    c = int(c) - 1
    w = int(w)
    if d == 'U':
        d = 0
    elif d == 'D':
        d = 1
    elif d == 'L':
        d = 2
    else:
        d = 3
    balls.append(Ball(r,c,d,w,n,num,0))


for _ in range(t):
    for ball in balls:
        ball.move()
    balls = collapse(balls)

print(len(balls), end=' ')
print(max(balls, key=lambda ball : ball.w).w)