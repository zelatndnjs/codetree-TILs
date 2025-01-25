num = list(map(int, input().split()))
print(abs(sum(num[::2])-sum(num[1::2])))