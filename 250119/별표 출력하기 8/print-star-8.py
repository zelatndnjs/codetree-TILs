n = int(input())
for i in range(n):
    if i%2==0:
        print('*')
    else:
        for j in range(i+1):
            print('*',end=' ')
        print()