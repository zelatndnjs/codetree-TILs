n= int(input())
direction = {'E':1, 'N':2, 'W':3 , 'S':4}
dx = [0,1,0,-1,0]
dy  = [0,0,1,0,-1]
x=0
y=0
for i in range(n):
    d, t = input().split()
    t = int(t)
    x += dx[direction[d]] * t
    y += dy[direction[d]] * t
print(x,y)