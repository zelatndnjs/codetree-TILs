n = int(input())
num = list(map(int, input().split()))
evennum = []
for i in num:
    if i%2==0:
        evennum.append(i)
evennum.reverse()
for i in evennum:
    print(i, end=' ')