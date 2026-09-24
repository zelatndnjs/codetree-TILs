from itertools import permutations

n = int(input())

arr = [i for i in range(1, n+1)]

a = list(permutations(arr, n))

a = reversed(a)

for i in a:
    print(*i)