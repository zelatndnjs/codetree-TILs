n = int(input())
num = list(map(int, input().split()))
chk = 0
pos = 0
for i in range(n-1,0,-1):
    if num[i] < num[i-1]:
        chk = 1
        pos = i
        break
if chk == 0:
    print(0)
else:
    print(pos)
