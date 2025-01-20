n = int(input())
if n%2==0:
    for i in range(n):
        for j in range(n):
            if (i==0) or (j%2==1 and i<=j):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
else:
    for i in range(n-1):
        for j in range(n):
            if (i==0) or (j%2==1 and i<=j):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()