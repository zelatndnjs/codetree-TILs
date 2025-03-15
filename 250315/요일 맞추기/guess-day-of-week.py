day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
m1, d1, m2, d2 = map(int, input().split())
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
print(date[difference%7])
