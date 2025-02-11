def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
a,b = map(int,input().split())

result = 0
for i in range(a,b+1):
    if isPrime(i):
        result += i

print(result)