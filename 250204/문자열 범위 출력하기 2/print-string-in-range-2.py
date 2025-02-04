a = input()
n = int(input())
if n >= len(a):
    name = a[::-1]
    print(name)
else:
    for i in range(n):
        print(a[-1-i], end='')