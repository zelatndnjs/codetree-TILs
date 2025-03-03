n = int(input())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
if set1 == set2:
    print("Yes")
else:
    print("No")