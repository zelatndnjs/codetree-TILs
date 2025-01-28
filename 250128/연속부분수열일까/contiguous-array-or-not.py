n1, n2 = map(int, input().split())
A = ''.join(list(input().split()))
B = ''.join(list(input().split()))
if A.find(B) == -1:
    print("No")
else:
    print("Yes")
