def f(a,b):
    cnt = 0
    for i in range(a,b+1):
        if isPrime(i) and isEven(i):
            cnt += 1
    return cnt

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def isEven(n):
    num = list(map(int, list(str(n))))
    if sum(num)%2==0:
        return True
    else:
        return False

a,b = map(int,input().split())
print(f(a,b))