n,q = map(int,input().split())
num = list(map(int,input().split()))
for i in range(q):
    seq = list(map(int,input().split()))
    if seq[0] == 1:
        print(num[seq[1]-1])
    elif seq[0] == 2:
        if seq[1] in num:
            print(num.index(seq[1])+1)
        else:
            print(0)
    else:
        for i in range(seq[1]-1, seq[2]):
            print(num[i], end=' ')
        print()