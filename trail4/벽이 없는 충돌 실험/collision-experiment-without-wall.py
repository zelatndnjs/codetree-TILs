class Ball:
    def __init__(self, x, y, w, d, n):
        self.x = 2*x
        self.y = 2*y
        self.w = w
        if d == "U":
            self.dx = 0
            self.dy = 1
        elif d == "D":
            self.dx = 0
            self.dy = -1
        elif d == "L":
            self.dx = -1
            self.dy = 0
        else:
            self.dx = 1
            self.dy = 0
        self.n = n

T = int(input())

def collapse(Balls):
    meeting = []
    for i in range(len(Balls)-1):
        for j in range(i+1, len(Balls)):
            if Balls[i].dx - Balls[j].dx == 0:
                if Balls[i].dy - Balls[j].dy == 0:
                    continue
                else:
                    t = (Balls[j].y - Balls[i].y) / (Balls[i].dy - Balls[j].dy)
                    if t >= 0 and Balls[i].x + Balls[i].dx*t == Balls[j].x + Balls[j].dx*t:
                        meeting.append((i,j,t))
            else:
                t = (Balls[j].x - Balls[i].x) / (Balls[i].dx - Balls[j].dx)
                if t >= 0 and Balls[i].y + Balls[i].dy*t == Balls[j].y + Balls[j].dy*t:
                    meeting.append((i,j,t))
            # Balls[i].x + Balls[i].dx*t == Balls[j].x + Balls[j].dx*t and Balls[i].y + Balls[i].dy*t == Balls[j].y + Balls[j].dy*t
    return meeting

def solve(Balls, meeting):
    lasttime = -1
    if len(meeting) == 0:
        return lasttime
    else:
        newmeeting = []
        meeting.sort(key=lambda x: x[2])
        lasttime = meeting[0][2]
        while True:
            if len(meeting) <= 0:
                break
            x, y, t = meeting[0]
            lasttime = t
            die = 0
            if Balls[x].w > Balls[y].w:
                die = y
            elif Balls[x].w < Balls[y].w:
                die = x
            else:
                if x > y:
                    die = y
                else:
                    die = x
            for meet in meeting:
                if meet[0] != die and meet[1] != die:
                    newmeeting.append(meet)
            meeting = newmeeting
            newmeeting = []
        return lasttime

for t in range(T):
    Balls = []
    N = int(input())
    for n in range(N):
        x,y,w,d = input().split()
        Balls.append(Ball(int(x), int(y), int(w), d, n+1))
    meeting = collapse(Balls)
    lasttime = solve(Balls,meeting)
    print(int(lasttime))