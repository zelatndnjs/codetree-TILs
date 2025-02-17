def dividedTwo(arr):
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            arr[i] = arr[i]//2
    return arr

N = int(input())
arr = list(map(int, input().split()))
arr = dividedTwo(arr)
for i in arr:
    print(i, end=' ')