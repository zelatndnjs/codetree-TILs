# n, k = map(int, input().split())
# block = [0 for _ in range(n+1)]
# for i in range(k):
#     a,b = map(int, input().split())
#     for j in range(a,b+1):
#         block[j] += 1

# print(max(block))

n, k = map(int, input().split())
block = [0 for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a-1,b-1):
        block[i] += 1
print(block.max)