n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
x = n-1
y = n-1
chk = 0
for num in range(1, n*n+1):
  if chk == 0:
    arr[y][x] = num
    y -= 1
    if y <0:
      y=0
      chk = 1
      x -= 1
  else:
    arr[y][x] = num
    y += 1
    if y == n:
      y = n-1
      chk = 0
      x -= 1
for i in range(n):
  for j in range(n):
    print(arr[i][j], end=' ')
  print()