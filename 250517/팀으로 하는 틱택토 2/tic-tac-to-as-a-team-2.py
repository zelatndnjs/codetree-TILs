cube = [input() for i in range(3)]

def istic(a,b,c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and a != b:
        return True
    else:
        return False
cnt = 0
if istic(cube[0][0], cube[0][1], cube[0][2]):
    cnt += 1
if istic(cube[1][0], cube[1][1], cube[1][2]):
    cnt += 1
if istic(cube[2][0], cube[2][1], cube[2][2]):
    cnt += 1
for i in range(3):
    if istic(cube[0][i], cube[1][i], cube[2][i]):
        cnt += 1
if istic(cube[0][0], cube[1][1], cube[2][2]):
    cnt += 1
if istic(cube[2][0], cube[1][1], cube[0][2]):
    cnt += 1
print(cnt)