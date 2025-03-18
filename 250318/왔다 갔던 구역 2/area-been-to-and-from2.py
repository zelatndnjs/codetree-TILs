point = 1000
n = int(input())
line = [0 for _ in range(2000)]
for i in range(n):
    num, direction = input().split()
    num = int(num)
    if direction == 'L':
        for j in range(point-1, point-num-1, -1):
            line[j] += 1
        point -= num
    else:
        for j in range(point, point+num):
            line[j] += 1
        point += num
print(len(line) - line.count(0) - line.count(1))