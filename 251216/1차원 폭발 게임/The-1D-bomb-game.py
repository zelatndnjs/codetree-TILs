n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
while True:
    count = 1
    start = 0
    chk = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            count += 1
        else:
            if count >= m:
                chk = 1
                for j in range(count):
                    arr.pop(start)
                count = 0
                break
            count = 1
            start = i+1
    if count >= m:
        chk = 1
        for j in range(count):
            arr.pop(start)
    if chk == 0:
        break
print(len(arr))
for i in arr:
    print(i)