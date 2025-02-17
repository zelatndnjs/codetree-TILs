def isPal(string):
    reverseString = string[::-1]
    if string == reverseString:
        return True
    else:
        return False

A = input()
if isPal(A):
    print("Yes")
else:
    print("No")