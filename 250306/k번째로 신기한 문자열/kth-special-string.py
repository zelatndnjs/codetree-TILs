n,k,t = input().split()
n = int(n)
k = int(k)
arr = []
for i in range(n):
    string = input()
    if string.startswith(t):
        arr.append(string)
arr.sort()
print(arr[k-1])
