a = input()
b = input()
num1 = ""
for i in a:
    if i.isdigit():
        num1 += i
num1 = int(num1)

num2 = ""
for i in b:
    if i.isdigit():
        num2 += i
num2 = int(num2)

print(num1+num2)