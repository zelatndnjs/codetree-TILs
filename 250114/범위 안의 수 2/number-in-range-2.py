result = 0
cnt = 0
for i in range(10):
    num = int(input())
    if 0<=num<=200:
        result += num
        cnt += 1
print(result, result/cnt)