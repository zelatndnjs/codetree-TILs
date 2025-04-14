a = list(input())
for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        break
num = int(''.join(a), 2)
print(num)