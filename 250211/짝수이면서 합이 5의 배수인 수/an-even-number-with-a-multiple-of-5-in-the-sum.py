def isTwo(n):
    return n%2==0

def isFive(n):
    return sum(list(map(int, list(str(n))))) % 5 == 0

n = int(input())
if isTwo(n) and isFive(n):
    print("Yes")
else:
    print("No")