arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
for i in range(2):
    a,b = map(int, input().split())
    arr = arr[:a-1:] + arr[b::]
print(len(arr))
for i in range(len(arr)):
    print(arr[i])