num = list(map(int, input().split()))
result = []
for i in num:
    if i%3==0:
        break
    else:
        result.append(i)
print(result.pop())