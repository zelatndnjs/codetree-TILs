def countOnjun(a,b):
    cnt = 0
    for i in range(a,b+1):
        if isOnjun(i):
           cnt += 1
    return cnt
def isOnjun(n):
    if n%2 ==0:
        return False
    elif n%10 == 5:
        return False
    elif n%3==0 and n%9!=0:
        return False
    else:
        return True

a,b = map(int,input().split())
print(countOnjun(a,b))