num = list(map(int, input().split()))

realnum = list()
for i in num:
    if i==0:
        break
    else:
        realnum.append(i)

print(f"{realnum[-1]+realnum[-2]+realnum[-3]}")