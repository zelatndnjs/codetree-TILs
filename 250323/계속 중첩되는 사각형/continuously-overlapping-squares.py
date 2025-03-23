def printplain(plain):
    for i in range(201):
        for j in range(201):
            print(plain[i][j], end="")
        print()
n = int(input())
plain =[[0 for i in range(201)] for j in range(201)]
chk = 0
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    if chk ==0:
        for j in range(x1, x2):
            for k in range(y1, y2):
                plain[j][k] = 1
        chk = 1
    else:
        for j in range(x1, x2):
            for k in range(y1, y2):
                plain[j][k] = 2
        chk = 0
    # printplain(plain)

result = 0
for i in range(201):
    for j in range(201):
        if plain[i][j] == 2:
            result += 1
print(result)