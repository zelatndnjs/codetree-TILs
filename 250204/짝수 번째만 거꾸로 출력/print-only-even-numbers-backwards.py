a = input()
result =""
for i in range(len(a)):
    if i%2!=0:
        result += a[i]
    else:
        continue

new = result[::-1]
print(new)