n = int(input())
cnt = 65
for i in range(1,n+1):
    for j in range(i):
        if cnt == 91:
            cnt = 65
        print(chr(cnt), end='')
        cnt += 1
    print()