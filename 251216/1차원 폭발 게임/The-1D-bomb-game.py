n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.append(-1)
while True:
    starts = []
    ends = []
    newarr = []
    count = 1
    start = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            count += 1
        else:
            if count >= m:
                starts.append(start)
                ends.append(i)
            start = i+1
            count = 1
    if len(starts) == 0:
        break
    else:
        for i in range(len(arr)):
            chk = 0
            for j in range(len(starts)):
                if i >= starts[j] and i <= ends[j]:
                    chk = 1
            if chk == 0:
                newarr.append(arr[i])
        arr = newarr
arr.pop(-1)
print(len(arr))
for i in arr:
    print(i)