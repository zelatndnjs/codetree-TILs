def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * f(n-1)

n = int(input())
print(f(n))