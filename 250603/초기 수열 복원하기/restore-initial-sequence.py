n = int(input())
a = list(map(int, input().split()))
num = []
for first in range(1, a[0]):
    num = []
    num.append(first)
    j = 0
    chk = 0
    for i in a:
        if i-num[j] <= 0 or i-num[j] in num:
            chk = 1
            break
        else:
            num.append(i-num[j])
            j += 1
    if chk == 0:
        for i in num:
            print(i, end=' ')