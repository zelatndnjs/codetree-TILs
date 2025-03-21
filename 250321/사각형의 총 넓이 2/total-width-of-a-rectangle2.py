n= int(input())
area = [[0 for _ in range(201)] for _ in range(201)]
square = 0
for i in range(n):
    a,b,c,d = map(int,input().split())
    a += 100
    b += 100
    c += 100
    d += 100
    for j in range(b,d):
        for k in range(a,c):
            if area[j][k] == 0:
                square += 1
                area[j][k] = 1
print(square)