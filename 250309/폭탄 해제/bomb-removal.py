class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

a,b,c = input().split()
c = int(c)
bomb1 = Bomb(a,b,c)
print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.second}")