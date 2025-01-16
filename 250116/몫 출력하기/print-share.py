cnt = 0
while True:
    if cnt == 3:
        break
    num = int(input())
    if num % 2== 1:
        continue
    else:
        cnt += 1
        print(num//2)
