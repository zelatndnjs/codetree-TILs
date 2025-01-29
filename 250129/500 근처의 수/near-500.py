num = list(map(int, input().split()))
a = [i for i in num if i>500]
b = [i for i in num if i<500]
print(max(b), min(a))
