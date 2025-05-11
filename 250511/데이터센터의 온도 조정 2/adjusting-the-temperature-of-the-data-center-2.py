N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
m = 0
for i in range(0,1001):
    abil = 0
    for j in ranges:
        if i < j[0]:
            abil += C
        elif i <= j[1]:
            abil += G
        else:
            abil += H
    if m < abil:
        m = abil
print(m)