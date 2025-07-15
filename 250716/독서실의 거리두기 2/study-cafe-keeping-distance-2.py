n = int(input())
seats = input()
pos = []
dis = []
for i in range(n):
    if seats[i] == '1':
        pos.append(i)
for i in range(len(pos)-1):
    dis.append(pos[i+1] - pos[i])
if len(dis) == 0:
    print(max(pos[0], n-1 - pos[-1]))
else:
    print(min(min(dis), max(max(dis)//2, pos[0], n - 1 - pos[-1])))