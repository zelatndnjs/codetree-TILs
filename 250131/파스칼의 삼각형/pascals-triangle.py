def comb(a,b):
  n = a
  r = min(b, a-b)
  if r == 0:
    return 1
  else:
    up = 1
    for i in range(r):
      up *= n
      n -= 1
    down = 1
    for j in range(1,r+1):
      down *= j
    return up//down

n = int(input())
for i in range(n):
  for j in range(i+1):
    print(comb(i,j), end=' ')
  print()