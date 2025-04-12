n = int(input())
A = list(map(int, input().split()))
distances = []
for i in range(n):
    distance = 0
    for j in range(n):
        distance += abs(j-i) * A[j]
    distances.append(distance)
print(min(distances))
