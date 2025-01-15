cnt = 0
n = int(input())
i = 1
while True:
    if n <= 1:
        break
    n //= i
    cnt += 1
    i += 1

print(cnt)