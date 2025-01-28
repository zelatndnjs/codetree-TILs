N = int(input())
num = list(map(int, input().split()))
result = [-1]
for i in num:
    if num.count(i) == 1:
        result.append(i)
print(max(result))