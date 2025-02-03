n = int(input())
cnt = 0
l = 0
for i in range(n):
    a = input()
    l += len(a)
    if a[0] == 'a':
        cnt += 1
print(f"{l} {cnt}")