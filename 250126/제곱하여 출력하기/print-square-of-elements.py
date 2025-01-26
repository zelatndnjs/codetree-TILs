n = int(input())
num = list(map(int, input().split()))
newnum = [i**2 for i in num]
for i in newnum:
    print(i,end=' ')