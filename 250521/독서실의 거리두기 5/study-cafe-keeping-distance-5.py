n = int(input())
seat = list(input())
ans = 0
for i in range(n):
    if seat[i] == '1':
        continue
    else:
        range1 = 0
        for j in range(i, -1, -1):
            range1 += 1
            if seat[j] == '1':
                break
        range2 = 0
        for j in range(i+1, n):
            range2 += 1
            if seat[j] == '1':
                break
        maxrange = min(range1, range2)
        ans = max(maxrange, ans)
print(ans)