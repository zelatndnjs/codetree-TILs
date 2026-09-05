from itertools import combinations

n, m = map(int, input().split())

pool = [i for i in range(1, n+1)]

answer = list(combinations(pool, m))

for i in answer:
    print(*i)