N = int(input())
arr = [i for i in range(1,N+1)]
while True:
    if len(arr) == 1:
        break
    arr.pop(0)
    arr.append(arr.pop(0))
print(arr[0])