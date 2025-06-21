n,m,p = map(int, input().split())
programmers = [0 for i in range(n)]
for i in range(m):
    programmer, num = input().split()
    num = int(num)
    if i >= p-1:
        programmers[ord(programmer) - ord('A')] = 1
for i in range(n):
    if programmers[i] == 0:
        print(chr(i+65), end=' ')