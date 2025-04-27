n, k = map(int, input().split())
candies = [0 for i in range(301)]
m = 0
for i in range(n):
    a,b = map(int, input().split())
    b += 100
    if candies[b] == 0:
        candies[b] = a
    else:
        candies[b] += a
for c in range(100, 201):
    # print(c-k, c+k, sum(candies[c-k:c+k+1]))
    if m < sum(candies[c-k:c+k+1]):
        m = sum(candies[c-k:c+k+1])
print(m)