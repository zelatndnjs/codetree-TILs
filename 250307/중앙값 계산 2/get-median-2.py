n = int(input())
num = []
chk = 0
arr = list(map(int, input().split()))
for i in range(n):
    num.append(arr[i])
    num.sort()
    if chk == 0:
        print(num[len(num)//2], end=' ')
        chk = 1
    else:
        chk = 0
        continue