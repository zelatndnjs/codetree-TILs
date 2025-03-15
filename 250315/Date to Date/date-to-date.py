a,b,c,d = map(int,input().split())
day= [0,31,28,31,30,31,30,31,31,30,31,30,31]
secondday = 0
for i in range(c):
    secondday += day[i]
secondday += d
firstday = 0
for i in range(a):
    firstday += day[i]
firstday += b
print(secondday - firstday + 1)