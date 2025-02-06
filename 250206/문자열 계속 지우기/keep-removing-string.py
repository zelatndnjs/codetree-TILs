a = input()
b = input()
while True:
    if b not in a:
        print(a)
        break
    else:
        first = a.index(b)
        a = a[:first:] + a[first+len(b)::]