num = list(map(int, input().split()))
num.sort()
abcd = num[-1]
a = num[0]
b = num[1]
c = num[2]
d = abcd - a-b-c
print(a,b,c,d)