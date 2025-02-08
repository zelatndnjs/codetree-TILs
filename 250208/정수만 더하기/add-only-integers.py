a = input()
result = 0
for i in a:
    if i.isdigit():
        result += int(i)
print(result)