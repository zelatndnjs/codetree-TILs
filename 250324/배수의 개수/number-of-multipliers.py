three = 0
five = 0
for i in range(10):
    num = int(input())
    if num % 3 == 0:
        three += 1
    if num % 5 == 0:
        five += 1
print(three, five)