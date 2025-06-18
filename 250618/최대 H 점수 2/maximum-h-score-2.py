n, l =map(int, input().split())
num = list(map(int, input().split()))
h = 1
ans = 1
while True:
    cnt1 = 0
    cnt2 = 0
    for i in num:
        if i>= h:
            cnt1 += 1
        elif i >= h-1:
            cnt2+= 1
    if cnt1 >= h:
        h += 1
        continue
    elif cnt1 + min(l, cnt2) >= h:
        h += 1
        continue
    else:
        ans = h - 1
        break
print(ans)