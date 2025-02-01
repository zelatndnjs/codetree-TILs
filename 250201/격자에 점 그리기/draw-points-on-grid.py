n,m = map(int, input().split())

arr = [[0 for i in range(n)]for j in range(n)]

for i in range(m):
  a,b = map(int, input().split())
  arr[a-1][b-1] = i+1

for i in range(n):
  for j in range(n):
    print(arr[i][j], end=' ')
  print()