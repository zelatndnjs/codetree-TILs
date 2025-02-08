N = int(input())
result = 0
for i in range(N):
    num = int(input())
    result += num
result = str(result)
result = result[1::] + result[0]
print(result)