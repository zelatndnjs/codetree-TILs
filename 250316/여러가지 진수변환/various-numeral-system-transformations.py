n,b = map(int, input().split())
def f(n,b):
    result = []
    while True:
        result.append(str(n%b))
        if n < b:
            break
        n//=b
    result.reverse()
    return ''.join(result)

print(f(n,b))