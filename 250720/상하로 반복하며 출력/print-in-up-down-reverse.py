n = int(input())
s = [[0 for i in range(n)] for j in range(n)]
num = 1
i = 0
j = 0
chk = 0
for k in range(n*n):
    s[i][j] = num
    num += 1
    if chk == 0:
        i += 1
        if i >= n:
            chk = 1
            j += 1
            num = 1
            i = n -1
    else:
        i -= 1
        if i < 0:
            chk = 0
            j += 1
            num = 1
            i = 0
for i in range(n):
    for j in range(n):
        print(s[i][j], end='')
    print()