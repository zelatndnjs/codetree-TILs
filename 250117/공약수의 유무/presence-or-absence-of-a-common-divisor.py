a,b = map(int,input().split())
chk = 0
for i in range(a,b+1):
    if 1920 % i ==0 and 2880 % i == 0:
        print(1)
        chk = 1
        break
        
if chk == 0:
    print(0)