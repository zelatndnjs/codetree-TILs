a = input()
result = ""
for i in a:
    if i.isalpha():
        result += i.upper()
print(result)