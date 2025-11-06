N, M = map(int, input().split())
cube = [list(map(int, input().split())) for i in range(N)]

def chk1(cube):
    num = 0
    for i in range(N-1):
        for j in range(M-1):
           num = max(num, cube[i+1][j] + cube[i+1][j+1] + cube[i][j+1],cube[i][j] + cube[i+1][j+1] + cube[i][j+1], cube[i][j] + cube[i+1][j] + cube[i][j+1], cube[i][j] + cube[i+1][j] + cube[i+1][j+1])
    return num

def chk2(cube):
    num = 0
    for i in range(N-2):
        for j in range(M):
            num = max(num, cube[i][j] + cube[i+1][j] + cube[i+2][j])
    for i in range(N):
        for j in range(M-2):
            num = max(num, cube[i][j] + cube[i][j+1] + cube[i][j+2])
    return num

print(max(chk1(cube), chk2(cube)))