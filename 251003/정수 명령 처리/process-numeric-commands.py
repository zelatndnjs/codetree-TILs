N = int(input())
arr = []
for i in range(N):
    m = input()
    if m[-1] >= '0' and m[-1] <= '9':
        a,b = m.split()
        arr.append(b)
    else:
        if m =='pop':
            print(arr.pop(-1))
        elif m =='size':
            print(len(arr))
        elif m == 'empty':
            if len(arr) == 0:
                print(1)
            else:
                print(0)
        elif m == 'top':
            print(arr[-1])