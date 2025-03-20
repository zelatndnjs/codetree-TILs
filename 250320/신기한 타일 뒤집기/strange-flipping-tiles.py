tiles = [0 for _ in range(200000)]
cur = 100000
n = int(input())
for i in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'L':
        for j in range(cur, cur-x, -1):
            tiles[j] = 1
        cur -= x -1
    else:
        for j in range(cur, cur+x):
            tiles[j] = 2
        cur += x -1
print(tiles.count(1), tiles.count(2))