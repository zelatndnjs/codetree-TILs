n,m,p = map(int, input().split())
arr = [tuple(input().split()) for _ in range(m)]
programmers = [0 for i in range(n)]
a = 0
for i in range(p-1, 0, -1):
    if arr[i][1] == arr[i-1][1]:
        continue
    else:
        p = i+1
        break
chk = 0
for i in range(m):
    programmer, num = arr[i]
    num = int(num)
    if num == 0:
        chk = 1
        break
    if i >= p - 1:
        programmers[ord(programmer) - ord('A')] = 1
if chk == 1:
    print()
else:
    for i in range(n):
        if programmers[i] == 0:
            print(chr(i+65), end=' ')