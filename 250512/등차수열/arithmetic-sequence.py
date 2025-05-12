n = int(input())
num = list(map(int, input().split()))
big = max(num)
cnt = []
for k in range(1, big):
    s = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(k-num[i]) == abs(k-num[j]) and i != j:
                # print(f"k는 {k}, i는 {num[i]}, j는 {num[j]}")
                s += 1
    cnt.append(s)
print(max(cnt))