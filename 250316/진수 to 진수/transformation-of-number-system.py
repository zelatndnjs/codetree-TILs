a,b = map(int,input().split())
n = int(input())
num = int(str(n), a)
def f(n,b):
    result = []
    while True:
        if n<b:
            result.append(str(n))
            break
        result.append(str(n%b))
        n = n//b
    result.reverse()
    return ''.join(result)

print(f(num,b))