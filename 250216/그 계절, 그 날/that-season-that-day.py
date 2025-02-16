def isYoon(y):
    if y % 400 ==0:
        return True
    elif y % 100 ==0:
        return False
    elif y % 4 ==0:
        return True
    else:
        return False

def isDate(y,m,d):
    if isYoon(y):
        if m >= 1 and m <= 12:
            if m==1 or m==3 or m==5 or m==7 or m== 8 or m== 10 or m== 12:
                if d>=1 and d<=31:
                    return True
                else:
                    return False
            elif m==2:
                if d>=1 and d<=29:
                    return True
                else:
                    return False
            else:
                if d>=1 and d<= 30:
                    return True
                else:
                    return False
        else:
            return False
    else:
        if m >= 1 and m <= 12:
            if m==1 or m==3 or m==5 or m==7 or m== 8 or m== 10 or m== 12:
                if d>=1 and d<=31:
                    return True
                else:
                    return False
            elif m==2:
                if d>=1 and d<=28:
                    return True
                else:
                    return False
            else:
                if d>=1 and d<= 30:
                    return True
                else:
                    return False
        else:
            return False

y,m,d = map(int,input().split())
if isDate(y,m,d):
    if m >= 3 and m <= 5:
        print("Spring")
    elif m>= 6 and m <= 8:
        print("Summer")
    elif m>= 9 and m <= 11:
        print("Fall")
    else:
        print("Winter")
else:
    print(-1)