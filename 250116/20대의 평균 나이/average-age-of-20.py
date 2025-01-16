l = list()
while True:
    num = int(input())
    if num >= 30 or num <= 19:
        print(f"{sum(l)/len(l):.2f}")
        break
    else:
        l.append(num)