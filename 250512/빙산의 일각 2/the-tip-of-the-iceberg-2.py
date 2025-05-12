n = int(input())
h = [int(input()) for _ in range(n)]
h.append(0)
big = max(h)
cnt = []
for level in range(1, big):
    s = 0
    for i in range(n):
        if h[i] - level >0 and h[i+1] - level <= 0:
            s += 1
    cnt.append(s)
print(max(cnt))
