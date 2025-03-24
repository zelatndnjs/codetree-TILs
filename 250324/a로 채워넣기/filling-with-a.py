a = input()
result = a[:1:] + 'a' + a[2:-2] + 'a' + a[-1]
print(result)