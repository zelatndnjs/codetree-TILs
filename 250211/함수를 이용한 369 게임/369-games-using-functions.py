def threeSixNine(A,B):
    cnt = 0
    for i in range(A, B+1):
        if isThreeSixNine(i) or isMultiplyThree(i):
            cnt += 1
    return cnt

def isThreeSixNine(n):
    return '3' in str(n) or '6' in str(n) or '9' in str(n)

def isMultiplyThree(n):
    return n%3==0

A, B = map(int, input().split())
print(threeSixNine(A,B))
