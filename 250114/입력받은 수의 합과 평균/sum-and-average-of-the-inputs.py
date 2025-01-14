n = int(input())

result = []

for i in range(n):
    num = int(input())
    result.append(num)

print(f"{sum(result)} {sum(result)/len(result):.1f}")