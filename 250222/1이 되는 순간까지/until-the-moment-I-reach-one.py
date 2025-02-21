n = int(input())
cnt = 0
while True:
    if n ==1:
        break
    if n%2==0:
        cnt += 1
        n //= 2
    else:
        cnt += 1
        n //= 3
print(cnt)