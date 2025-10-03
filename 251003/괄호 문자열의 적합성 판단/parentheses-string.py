s = []
m = input()
chk = 0
for i in m:
    if i =='(':
        s.append('(')
    else:
        if len(s) == 0:
            chk = 1
            break
        s.pop(-1)

if len(s) != 0:
    chk = 1
        
if chk == 1:
    print("No")
else:
    print("Yes")