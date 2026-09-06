from itertools import product

k, n = map(int, input().split())

arr = [i for i in range(1, k+1)]

p = list(product(arr, repeat=n))

for i in p:
    print(*i)