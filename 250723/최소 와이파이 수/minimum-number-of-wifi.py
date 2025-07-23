n, m = map(int, input().split())
people = list(map(int, input().split()))
wifi = 0
wifipos = -101
for i in range(n):
    if people[i] == 1:
        if i >= wifipos - m and i <= wifipos +m:
            continue
        else:
            wifipos = i + m
            wifi += 1
print(wifi)
