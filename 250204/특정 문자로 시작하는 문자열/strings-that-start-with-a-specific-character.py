n = int(input())
a = list()
for i in range(n):
    a.append(input())
b = input()
rotn = 0
rlfdl = 0
for i in a:
    if i[0] == b:
        rotn += 1
        rlfdl += len(i)
print(f"{rotn} {rlfdl/rotn:.2f}")