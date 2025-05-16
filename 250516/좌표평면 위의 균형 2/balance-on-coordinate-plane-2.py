n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]
xset = set()
yset = set()
for dot in dots:
    xset.add(dot[0])
    yset.add(dot[1])
minx = min(xset) - 1
maxx = max(xset) + 1
miny = min(yset) - 1
maxy = max(yset) + 1
diff = []
ans = []
for x in range(minx, maxx+1, 2):
    for y in range(miny, maxy+1, 2):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        for dot in dots:
            if dot[0] > x and dot[1] > y:
                cnt1 += 1
            elif dot[0] < x and dot[1] > y:
                cnt2 += 1
            elif dot[0] < x and dot[1] < y:
                cnt3 += 1
            elif dot[0] > x and dot[1] < y:
                cnt4 += 1
            else:
                print("Error")
                
        diff.append(max(cnt1, cnt2, cnt3, cnt4) - min(cnt1,cnt2,cnt3,cnt4))
        ans.append(max(cnt1, cnt2, cnt3, cnt4))
idx = diff.index(min(diff))
print(min(ans))
                