a = input()
seq = input()
l = seq.count('L')
r = seq.count('R')
if l > r:
    for i in range(l-r):
        a = a[1:] + a[0]
elif r< l:
    for i in range(r-l):
        a = a[-1] + a[:-1:]

print(a)