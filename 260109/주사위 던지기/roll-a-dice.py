n,m,r,c = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
r -= 1
c -= 1
grid[r][c] = 6
directions = list(input().split())
dice = [6,2,3,5,4,1]
Ldice = [4,2,6,5,1,3]
Rdice = [3,2,1,5,6,4]
Udice = [5,6,3,1,4,2]
Ddice = [2,1,3,6,4,5]

def isin(n,r,c):
    return r>= 0 and r < n and c>=0 and c <n

def roll(dice, direction):
    if direction == 'U':
        newdice = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]
    elif direction == 'D':
        newdice = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]
    elif direction == 'L':
        newdice = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]
    else:
        newdice = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]
    return newdice

for direction in directions:
    if direction == 'U':
        if isin(n,r-1,c):
            r -= 1
            dice = roll(dice, direction)
            grid[r][c] = dice[0]
    elif direction == 'D':
        if isin(n,r+1,c):
            r += 1
            dice = roll(dice, direction)
            grid[r][c] = dice[0]
    elif direction == 'L':
        if isin(n,r,c-1):
            c -= 1
            dice = roll(dice, direction)
            grid[r][c] = dice[0]
    else:
        if isin(n,r,c+1):
            c += 1
            dice = roll(dice, direction)
            grid[r][c] = dice[0]

answer = sum([sum(x) for x in grid])

print(answer)
