def isyun(year):
    if year % 100 == 0 and year % 400 !=0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

n = int(input())
cnt = 0
for i in range(1,n+1):
    if isyun(i):
        cnt += 1

print(cnt)