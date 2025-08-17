n,m = map(int, input().split())
ans = '0'
str = input()
for i in str:
    ans = ans + i + '0'
str = ans
idx = len(ans)-1
for i in range(m):
    com = input()
    if com[0] == 'P':
        a,b = com.split()
        str = str[:idx:] + '0' + b + str[idx::]
        idx += 2
        if idx >= len(str):
            idx = len(str)-1
    elif com == 'L':
        idx -= 2
        if idx < 0 :
            idx = 0
    elif com == 'R':
        idx += 2
        if idx >= len(str):
            idx = len(str)-1
    elif com == 'D':
        str = str[:idx:] + str[idx+2::]
ans = ''
for i in range(1,len(str), 2):
    ans += str[i]
print(ans)