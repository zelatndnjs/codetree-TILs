n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a,b = zip(*moves)
a = list(a)
b = list(b)
ans = []
# 1 = 주먹 2 = 가위 3 = 보
num = 0
for i in moves:
    c, d = i
    if c == 1 and d == 2 or c == 2 and d == 3 or c == 3 and d == 1:
        num+= 1
ans.append(num)
num = 0
# 1 = 주먹 2 = 보 3 = 가위
for i in moves:
    c, d = i
    if c == 1 and d == 3 or c == 2 and d == 1 or c == 3 and d == 2:
        num+= 1
ans.append(num)
num = 0
# 1 = 가위 2 = 주먹 3 = 보
for i in moves:
    c, d = i
    if c == 1 and d == 3 or c == 2 and d == 1 or c == 3 and d == 2:
        num+= 1
ans.append(num)
num = 0
# 1 = 가위 2 = 보 3 = 주먹
for i in moves:
    c, d = i
    if c == 1 and d == 2 or c == 2 and d == 3 or c == 3 and d == 1:
        num+= 1
ans.append(num)
num = 0
# 1 = 보 2 = 주먹 3 = 가위
for i in moves:
    c, d = i
    if c == 1 and d == 2 or c == 2 and d == 3 or c == 3 and d == 1:
        num+= 1
ans.append(num)
num = 0
# 1 = 보 2 = 가위 3 = 주먹
for i in moves:
    c, d = i
    if c == 1 and d == 3 or c == 2 and d == 1 or c == 3 and d == 2:
        num+= 1
ans.append(num)
num = 0
print(max(ans))