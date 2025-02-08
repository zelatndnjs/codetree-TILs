a = input()
result = ""
for i in a:
    if 'a' <= i and i <= 'z':
        result += i.upper()
    elif 'A' <= i and i <= 'Z':
        result += i.lower()
print(result)