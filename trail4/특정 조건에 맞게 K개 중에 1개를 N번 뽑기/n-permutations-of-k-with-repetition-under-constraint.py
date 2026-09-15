from itertools import product

k, n = map(int, input().split())

arr = [i for i in range(1, k+1)]

result = list(product(arr, repeat=n))

for i in result:
    chk = 0
    if len(i) >= 3:
        for num in range(len(i)-2):
            if i[num] == i[num+1] == i[num+2]:
                chk = 1
                break
    if chk == 1:
        continue
    else:
        print(*i)
