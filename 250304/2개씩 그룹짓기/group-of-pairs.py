n = int(input())
arr = sorted(list(map(int, input().split())))
maxnum = 0
for i in range(n):
    if maxnum < arr[i] + arr[-1-i]:
        maxnum = arr[i] + arr[-1-i]
print(maxnum)