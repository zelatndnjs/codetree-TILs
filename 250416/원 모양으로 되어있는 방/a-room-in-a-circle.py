n = int(input())
rooms = [int(input()) for _ in range(n)]
distance = []
for i in range(n):
    newrooms = rooms[i:] + rooms[:i]
    d = 0
    for j in range(1, n):
        d += newrooms[j] *j
    distance.append(d)
print(min(distance))
