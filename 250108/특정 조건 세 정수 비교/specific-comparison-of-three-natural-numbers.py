a, b, c = map(int, input().split())
num = [a, b, c]
if a == min(num):
    print(1, end=' ')
else:
    print(0, end=' ')
if a==b and b==c:
    print(1)
else:
    print(0)