n = int(input())
num = list(map(int, input().split()))
for i in reversed(num):
    if i %2 ==0:
        print(i, end=' ')