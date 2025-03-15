day = [0,31,29,31,30,31,30,31,31,30,31,30,31]
m1, d1, m2, d2 = map(int, input().split())
d = input()
if d == 'Mon':
    d1 += 0
elif d == 'Tue':
    d1 += 1
elif d == 'Wed':
    d1 += 2
elif d == 'Thu':
    d1 += 3
elif d == 'Fri':
    d1 += 4
elif d == 'Sat':
    d1 += 5
else:
    d1 += 6

date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
firstday = 0
for i in range(m1):
    firstday += day[i]
firstday += d1
secondday = 0
for i in range(m2):
    secondday += day[i]
secondday += d2
difference = secondday - firstday
difference //= 7
print(difference+1)


