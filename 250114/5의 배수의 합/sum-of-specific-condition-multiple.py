a, b = map(int, input().split())

big = max(a, b)
small = min(a, b)

result = 0

for i in range(small, big + 1):
    if i % 5 == 0:
        result += i

print(result)