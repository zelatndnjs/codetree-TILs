n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
minlines = min(lines)[0]
maxlines = max(lines)[1]
for i in range(minlines, maxlines+1):
    chk = 0
    for j in lines:
        if i >= j[0] and i<=j[1]:
            pass
        else:
            chk = 1
            break
    if chk == 0:
        print("Yes")
        break
    else:
        continue
if chk==1:
    print("No")