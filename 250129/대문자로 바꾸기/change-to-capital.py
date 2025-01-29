for i in range(5):
    cha = list(input().split())
    for j in cha:
        print(chr(ord(j)-32), end=' ')
    print()