num = list(map(int, input().split()))
result = list()
for i in num:
    if i == 0:
        break
    else:
        if i % 2 == 0:
            result.append(i)
print(f"{len(result)} {sum(result)}")