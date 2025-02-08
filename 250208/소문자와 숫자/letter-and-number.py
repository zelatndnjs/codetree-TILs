a = input()
result = ""
for i in a:
    if i.isalpha():
        result += i.lower()
    elif i.isdigit():
        result += i
print(result)