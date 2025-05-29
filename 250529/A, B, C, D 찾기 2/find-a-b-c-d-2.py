num = list(map(int, input().split()))
num.sort()
a = min(num)
b = num[1]
ab = a+b
num.remove(ab)
num.remove(a)
num.remove(b)
c = min(num)
d = max(num) - a - b - c
print(a,b,c,d)