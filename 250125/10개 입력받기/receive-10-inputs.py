num = list(map(int, input().split()))
result = list()
for i in num:
    if i == 0:
        break
    else:
        result.append(i)
print(f"{sum(result)} {sum(result)/len(result):.1f}")