n = int(input())
seats = input()
chk= 0
if seats[0] == '0': # 맨 왼쪽만 0이면 1 오른쪽만 0이면 2 둘 다 0이면 3
    if seats[-1] == '0':
        chk = 3
    else:
        chk = 1
else:
    if seats[-1] == '0':
        chk = 2
pos = []
for i in range(n):
    if seats[i] == '1':
        pos.append(i)
dis = []
for i in range(len(pos)-1):
    dis.append(pos[i+1] - pos[i])
if chk == 0:
    print(max(dis)//2)
elif chk == 1:
    print(max(pos[0], max(dis)//2))
elif chk == 2:
    print(max((n-1) - pos[-1], max(dis)//2))
else:
    print(max((n-1) - pos[-1], pos[0], max(dis)//2))
