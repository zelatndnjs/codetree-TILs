n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
maxnum = ranges[0][1]//2

for num in range(1, maxnum+1):
    number = num
    chk = 0
    for r in ranges:
        number *= 2
        if number >= r[0] and number <= r[1]:
            pass
        else:
            chk = 1
            break
    if chk == 0:
        print(num)
        break

    