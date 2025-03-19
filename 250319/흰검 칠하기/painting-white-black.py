class Tile:
    def __init__(self,white=0,black=0, grey = 0, col = ''):
        self.white = white
        self.black = black
        self.grey = grey
        self.col = col
    def color(self):
        if self.white >= 2 and self.black >= 2:
            self.grey += 1
            self.col = 'grey'

cur = 50000
tiles = [Tile(white=0, black=0, grey=0, col='') for _ in range(100000)]
n = int(input())
for i in range(n):
    num, direction = input().split()
    num = int(num)
    if direction == 'R':
        for j in range(cur, cur+num):
            tiles[j].black += 1
            tiles[j].col = 'black'
            tiles[j].color()
        cur = cur+num-1
    else:
        for j in range(cur, cur-num, -1):
            tiles[j].white += 1
            tiles[j].col = 'white'
            tiles[j].color()
        cur = cur-num+1
black_count = sum(tile.col == 'black' for tile in tiles)
white_count = sum(tile.col == 'white' for tile in tiles)
grey_count = sum(tile.col == 'grey' for tile in tiles)

print(f"{white_count} {black_count} {grey_count}")