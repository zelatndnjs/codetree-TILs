def isAllSame(string):
    c = string[0]
    for i in range(1, len(string)):
        if string[i] == c:
            continue
        else:
            return False
    return True

A = input()
print("No" if isAllSame(A) else "Yes")