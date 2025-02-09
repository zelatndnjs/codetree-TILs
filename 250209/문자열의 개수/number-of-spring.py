sen = []
chk = 0
while True:
    A = input()
    if A == '0':
        break
    else:
        if chk %2!=0:
            chk += 1
            continue
        else:
            sen.append(A)
            chk += 1
print(chk)
for i in sen:
    print(i)
