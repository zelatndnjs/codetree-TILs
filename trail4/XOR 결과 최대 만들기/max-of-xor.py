from itertools import combinations

n, m = map(int, input().split())
A = list(map(int, input().split()))

c = combinations(A, m)

arr = []
for i in c:
    a = i[0]
    for j in range(1, len(i)):
        a = a ^ i[j]
    arr.append(a)

print(max(arr))
# Please write your code here.