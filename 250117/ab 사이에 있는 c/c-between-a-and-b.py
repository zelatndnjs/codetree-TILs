a,b,c = int(map, input().split())
cnt = 0
for i in range(a,b+1):
    if i % c == 0:
        print('YES')
        cnt = 1
        break

if cnt ==0:
    print('NO')