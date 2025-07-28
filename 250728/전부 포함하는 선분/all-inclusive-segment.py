n = int(input())
lines = [tuple(map(int, input().split())) for i in range(n)]
lines1 = sorted(lines, key=lambda x:x[0]) # 시작 기준 정렬
lines2 = sorted(lines, key=lambda x:x[1]) # 끝 기준 정렬
lines1.pop(0)
lines2.pop(-1)
lines1 = sorted(lines1, key=lambda x:x[0])
a = lines1[0][0]
lines1 = sorted(lines1, key=lambda x:x[1])
b = lines1[-1][1]
line1 = b-a

lines2 = sorted(lines2, key=lambda x:x[0])
a = lines2[0][0]
lines2 = sorted(lines2, key=lambda x:x[1])
b = lines2[-1][1]
line2 = b-a

print(min(line1, line2))