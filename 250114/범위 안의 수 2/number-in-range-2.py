result = 0

for i in range(10):
    num = int(input())
    if 0<=num<=200:
        result += num

print(result, result/10)