a = input()
for i in range(len(a)):
    if i%2==0:
        print(a[-1-i], end='')
    else:
        continue