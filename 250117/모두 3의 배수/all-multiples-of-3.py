chk = 0
for i in range(5):
    num = int(input())
    if num % 3 ==0:
        chk +=1

if chk == 5:
    print(1)
else:
    print(0)