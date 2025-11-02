N = int(input())
cube = [list(map(int, input().split())) for i in range(N)]
coin = 0
for i in range(N-3+1):
    for j in range(N-3+1):
        coin = max(coin, cube[i][j] + cube[i][j+1] + cube[i][j+2] + cube[i+1][j] + cube[i+1][j+1] + cube[i+1][j+2] + cube[i+2][j] + cube[i+2][j+1] + cube[i+2][j+2])
print(coin)