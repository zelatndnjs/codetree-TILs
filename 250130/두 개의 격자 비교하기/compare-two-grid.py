n,m = map(int,input().split())
arr1 = [list(map(int,input().split())) for i in range(n)]
arr2 = [list(map(int,input().split())) for i in range(n)]
result = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if arr1 [i][j] != arr2[i][j]:
            result[i][j] = 1

for i in range(n):
    for j in range(m):
        print(result[i][j],end=" ")
    print()