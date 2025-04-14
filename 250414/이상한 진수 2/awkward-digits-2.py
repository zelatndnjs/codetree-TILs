a = list(input())
chk = 0
for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        chk = 1
        break
if chk == 1:
    num = int(''.join(a), 2)
    print(num)
else:
    a[-1] ='0'
    num = int(''.join(a), 2)
    print(num)