n = int(input())
cnt = 0
num=n
while True:
    print(num, end=' ')
    if num%5==0:
        cnt+=1
    if cnt == 2:
        break
    num += n
