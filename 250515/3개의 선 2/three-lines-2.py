import copy

n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]
xset = set()
yset = set()
for i in dots:
    x,y = i
    xset.add(x)
    yset.add(y)
minx = min(xset)
miny = min(yset)
maxx = max(xset)
maxy = max(yset)
chk = 0
if len(xset) <= 3 or len(yset) <= 3:
    chk = 1
else:
    for x1 in range(minx, maxx):
        for x2 in range(x1+1, maxx+1):
            for y1 in range(miny, maxy+1):
                newdots = copy.deepcopy(dots)
                cnt = 0
                for dot in newdots:
                    if dot[0] == x1 or dot[0] == x2 or dot[1] == y1:
                        cnt += 1
                if len(dots) == cnt:
                    # print(f'x1 = {x1}, x2 = {x2}, y1 = {y1}')
                    chk = 1
    for x1 in range(minx, maxx+1):
        for y1 in range(miny, maxy):
            for y2 in range(y1+1, maxy+1):
                newdots = copy.deepcopy(dots)
                cnt = 0
                for dot in newdots:
                    if dot[0] == x1 or dot[1] == y1 or dot[1] == y2:
                        cnt += 1
                if len(dots) == cnt:
                    chk = 1
                    # print(f'x1 = {x1}, y1 = {y1}, y2 = {y2}')
print(chk)