from itertools import product

n,m,k = map(int, input().split())

m -= 1

dices = list(map(int, input().split()))

horses = [i for i in range(k)]

pro = product(horses, repeat=n)

answer = 0

horses_place = [0 for _ in range(k)]

for p in pro:
    for i in range(n):
        horses_place[p[i]] += dices[i]
    chk = 0
    for i in range(k):
        if horses_place[i] >= m:
            chk += 1
    if answer < chk:
        answer = chk
    chk = 0
    horses_place = [0 for _ in range(k)]

print(answer)