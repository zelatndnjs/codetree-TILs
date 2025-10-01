N, a = map(int, input().split())
num = 1
while num <= N:
    if num % a ==0:
        print(1)
    else:
        print(0)
    num += 1