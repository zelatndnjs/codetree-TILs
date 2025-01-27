a,b = map(int,input().split())
num = [0 for i in range(b)]
while True:
    if a<=1:
        break
    c = a//b
    d = a%b
    num[d] += 1
    a = c

result = 0
for i in num:
    result += i**2
print(result)