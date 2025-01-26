num = list(map(int, input().split()))
for i in num:
    if i==0:
        break
    elif i%2==0:
        print(i//2,end=' ')
    else:
        print(i+3,end=' ')