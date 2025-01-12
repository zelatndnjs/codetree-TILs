a,b =map(int,input().split())
c = a//b
result = ""
result += str(c)
result += "."
for _ in range(20):
    a *= 10
    c = (a//b) % 10
    result += str(c)
print(result)
