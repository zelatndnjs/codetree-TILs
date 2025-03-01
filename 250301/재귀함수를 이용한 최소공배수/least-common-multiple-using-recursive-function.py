def f(n, arr):
    if len(arr) == 1:
        return m(n, arr[0])
    else:
        a = m(n, arr[0])
        return f(a, arr[1:])
def m(a,b):
    big = max(a,b)
    small = min(a,b)
    plus = big
    while True:
        if big % small == 0:
            return big
        else:
            big += plus

n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(arr[0])
else:
    n = arr[0]
    arr = arr[1:]
    print(f(n, arr))