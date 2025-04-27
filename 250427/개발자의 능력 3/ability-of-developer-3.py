d = list(map(int, input().split()))
s = sum(d)
diff = []
for i in range(4):
    for j in range(i+1, 5):
        for k in range(j+1, 6):
            a = d[i]+d[j]+d[k]
            b = s - a
            diff.append(abs(a-b))
print(min(diff))