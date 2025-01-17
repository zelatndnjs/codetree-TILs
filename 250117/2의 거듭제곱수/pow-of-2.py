cnt = 0
n = int(input())
while True:
    if n == 1:
        break
    n = n //2
    cnt += 1

print(cnt)