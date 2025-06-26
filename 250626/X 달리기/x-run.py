x = int(input())
t = 0
num = 1
while True:
    if num**2 > x:
        num -= 1
        break
    else:
        num += 1
if x == num**2:
    t = 2*num-1
elif x <= num**2+num:
    t = 2*num
else:
    t = 2*num + 1
print(t)