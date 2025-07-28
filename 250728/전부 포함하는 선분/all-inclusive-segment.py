n = int(input())
lines = [tuple(map(int, input().split())) for i in range(n)]
lines.sort()
line1 = lines[-1][1] - lines[1][0]
line2 = lines[-2][1] - lines[0][0]
print(min(line1, line2))