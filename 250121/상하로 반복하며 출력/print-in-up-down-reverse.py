n = int(input())
num = [[0 for _ in range(n)] for _ in range(n)]
cnt = 1
a,b = 0,0
chk = 0
for _ in range(n):
    for _ in range(n):
        if chk ==0:
            num[a][b] = cnt
            cnt += 1
            if cnt > n:
                cnt = 1
            a += 1
            if a == n:
                chk = 1
                a -= 1
                b += 1


        else:
            num[a][b] = cnt
            cnt += 1
            if cnt > n:
                cnt = 1
            a -= 1
            if a < 0:
                a =0
                chk = 0
                b += 1
for i in range(n):
    for j in range(n):
        print(num[i][j],end="")
    print()