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

def istic2(a,b,c):
    if a == b and a != c:
        return min(a,c), max(a,c)
    elif a == c and a != b:
        return min(a,b), max(a,b)
    elif b == c and a != b:
        return min(a,b), max(a,b)
    else:
        return False
cnt = 0
teams = set()
if istic(cube[0][0], cube[0][1], cube[0][2]):
    cnt += 1
    a,b = istic2(cube[0][0], cube[0][1], cube[0][2])
    teams.add((a,b))
if istic(cube[1][0], cube[1][1], cube[1][2]):
    cnt += 1
    a,b = istic2(cube[1][0], cube[1][1], cube[1][2])
    teams.add((a,b))
if istic(cube[2][0], cube[2][1], cube[2][2]):
    a,b = istic2(cube[2][0], cube[2][1], cube[2][2])
    teams.add((a,b))
    cnt += 1
for i in range(3):
    if istic(cube[0][i], cube[1][i], cube[2][i]):
        cnt += 1
        a,b = istic2(cube[0][i], cube[1][i], cube[2][i])
        teams.add((a,b))
if istic(cube[0][0], cube[1][1], cube[2][2]):
    cnt += 1
    a,b = istic2(cube[0][0], cube[1][1], cube[2][2])
    teams.add((a,b))
if istic(cube[2][0], cube[1][1], cube[0][2]):
    cnt += 1
    a,b = istic2(cube[2][0], cube[1][1], cube[0][2])
    teams.add((a,b))
print(len(teams))