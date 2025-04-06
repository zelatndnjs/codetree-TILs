n = int(input())
square = [input() for _ in range(n)]
# 위에서 \ 만나면 -> 오른쪽 즉 좌회전, / 만나면 왼쪽 즉 우회전
# 오른쪽에서 \ 만나면 -> 위쪽 즉 우회전, / 만나면 아래쪽 즉 좌회전
# 아래에서 \ 만나면 -> 왼쪽 즉 좌회전, / 만나면 오른쪽 즉 우회전
# 왼쪽에서 \ 만나면 -> 아래 즉 우회전, / 만나면 위쪽 즉 좌회전

k = int(input())

def light(startdirection, mirror):
    #startdirection 0이면 위 1이면 오른쪽 2이면 아래 3이면 왼쪽
    changedirection = 0
    if mirror == '\\':
        if startdirection == 0:
            changedirection = 3
        elif startdirection == 1:
            changedirection = 2
        elif startdirection == 2:
            changedirection = 1
        else:
            changedirection = 0
    else:
        if startdirection == 0:
            changedirection = 1
        elif startdirection == 1:
            changedirection = 0
        elif startdirection == 2:
            changedirection = 3
        else:
            changedirection = 2
    return changedirection

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

if k<=n:
    startdirection = 0
    x = 0
    y = k-1
elif k<= 2*n:
    startdirection = 1
    x = k%n - 1
    y = n-1
elif k<=3*n:
    startdirection = 2
    x = n - 1
    y = n-1 - (k-1)%n
else:
    startdirection = 3
    x = n - 1 - (k-1)%n
    y = 0

cnt = 0
# print(f"현재 위치 {x} {y}, 방향 {startdirection}")

while True:
    if x<0 or x>= n or y<0 or y >= n:
        break
    changedirection = light(startdirection, square[x][y])
    cnt += 1
    x += dx[changedirection]
    y += dy[changedirection]
    startdirection = changedirection
    # print(f"현재 위치 {x} {y}, 방향 {startdirection}")
print(cnt)