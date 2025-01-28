N = int(input())
num = list(map(int, input().split()))
while True:
    a = num.index(max(num))
    print(a+1, end=' ')
    if a==0:
        break
    num = num[:a]