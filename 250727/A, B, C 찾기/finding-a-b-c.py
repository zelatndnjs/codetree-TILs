num = list(map(int, input().split()))
num.sort()
abc = num[-1]
bc = num[-2]
a = abc - bc
b = num[1]
c = bc - b
print(a,b,c)