n = int(input())

plist = []
for i in range(1, n):
    if n % i == 0:
        plist.append(i)

if sum(plist) == n:
    print("P")
else:
    print("N")