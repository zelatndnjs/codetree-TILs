arr = [list(map(int, input().split())) for _ in range(4)]
result = 0
for i in range(4):
    for j in range(4):
        if j<=i:
            result += arr[i][j]
print(result)