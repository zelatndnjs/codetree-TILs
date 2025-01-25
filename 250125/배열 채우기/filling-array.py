num = list(map(int, input().split()))
result = list()
for i in num:
    if i == 0:
        break
    else:
        result.append(i)
for i in reversed(result):
    print(i,end=' ')