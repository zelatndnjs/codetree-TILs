cnt = [0 for i in range(4)]
for i in range(3):
    a,b = input().split()
    b = int(b)
    if a == 'Y':
        if b>= 37:
            cnt[0] += 1
        else:
            cnt[2] += 1
    else:
        if b>= 37:
            cnt[1] += 1
        else:
            cnt[3] += 1
for i in cnt:
    print(i, end=' ')
if cnt[0] >= 2:
    print('E', end=' ')