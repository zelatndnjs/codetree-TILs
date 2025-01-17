n = int(input())
chk = 0
for i in range(2, n):
    if n % i == 0:
        print("C")
        chk =1
        break

if chk == 0:
    print("P")