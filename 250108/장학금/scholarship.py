a, b = map(int, input().split())
c = 0
if a>=90:
    if b>=95:
        c = 100000
    elif b>=90:
        c = 50000
print(c)