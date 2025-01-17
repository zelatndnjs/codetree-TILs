n = int(input())
chk = 0
for i in range(2, n):
    if n % i == 0:
        chk = 1
        print("C")
        break

if chk == 0:
    print("N")