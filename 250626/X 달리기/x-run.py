x = int(input())
v = 1
d = 0
t = 0
while True:
    if d >= x:
        break
    d += v
    t += 1
    if d < x//2:
        v += 1
    else:
        if v > 1:
           v -= 1
        else:
            v = 1
print(t)